#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PML Parser

Jared Patrick <jared.patrick@gmail.com> -- 06.18.2014
"""

# stdlib
import os
import re
import code

class PMLParser(object):
    """Utility to parse pml script files"""

    def __init__(self, pml_file='index.pml'):
        self.in_pml = False
        self.stream = ''
        self._exec = []
        self.indent = False
        self.indent_buffer = 0
        self.pml_file = pml_file
        self.code = ''


    def main(self):
        """Run the script"""

        self.user = raw_input("What is your name?: ")
        os.system('clear')
        self.read()
        # return the stream for rendering
        return self.stream


    def read(self):
        """Read the pml file and detect pml tags to pass to parser"""

        with open(self.pml_file, 'r') as pml_file:
            for line in pml_file.readlines():
                if self.in_pml:
                    if re.match(r'.*</pml>.*', line): # reached end of tag
                        self.exit()
                        continue
                    # in pml logic if </pml> closing tag has not been reached
                    self._exec.append(line.strip())
                    continue
                # _execute only if out of pml
                check_tag = re.match(r'.*<pml>(.*)', line)
                if check_tag:
                    # single line logic
                    try:
                        # regex match checks for text immediately after the
                        # opening <pml> tag
                        line = check_tag.groups()[0]
                        # if closing tag is on the same line, strip the closing
                        # tag and append the line to the _exec
                        if re.match(r'.*</pml>.*', line):
                            self._exec.append(re.sub('</pml>',
                                                     '',
                                                     line.strip()))
                            self.exit()
                            continue
                        elif len(line) > 0:
                            # closing tag not yet encountered. append normally
                            self._exec.append(line.strip())
                    except IndexError:
                        pass

                    # not on a single line, but in pml tag
                    self.in_pml = True
                else:
                    # no pml encountered, write html to stream
                    self.stream += line.strip() + '\n'


    def exit(self):
        """Exit the pml code block"""

        # break loop if closing pml is matched
        self.in_pml = False
        self.parse()
        self._exec = []


    def parse(self):
        """Parse the code in the pml block"""

        for snippet in self._exec:
            # empty string indicates a newline
            if snippet == '':
                self.indent = False
                self.indent_buffer = 0
            # indent text after :(semi-colon)
            elif self.indent == True:
                self.code += ('\t' * self.indent_buffer) + snippet
                # check for :(semi-colon) inside indented block to increment
                # the indent buffer
                if re.match(r'.*:$', snippet):
                    self.indent_buffer += 1
            # if indent is false, check that current does not end with :
            # (semi-colon)
            elif re.match(r'.*:$', snippet):
                self.code += snippet
                self.indent = True
                self.indent_buffer += 1
            # concatenate standard line
            else:
                self.code += snippet

            # add newline per iteration
            self.code += '\n'
        self.execute()


    def execute(self):
        """Execute the code block"""

        env = {'USER': self.user}
        source = code.compile_command(self.code, '<stdio>', 'exec')
        exec(source, env)
        
        try:
            self.stream += env['pml'] + '\n'
        except NameError:
            pass
        # pml set to '' to "flush the pml buffer"
        pml = ''

if __name__ == '__main__':
    PARSER = PMLParser('index.pml')
    print PARSER.main()
