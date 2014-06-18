<pml>
    pml = "\n*** Hello {} ***\n".format(USER)
</pml>

<html>
<p>
This is an example of a pml file
</p>
<pml>
    blue = True

    # nesting examples
    def hello():
        if True:
            if blue:
                if True and blue:
                    if False:
                        pass # some code
                    return "<h2>Hello, World!</h2>"

    def hello_again():
        return "<h1>See you later!</h1>"

    pml = "Let me start by saying... {}".format(hello())
</pml>
<div>
    <pml>pml = "<a href=\"http://www.mypml.com\">Inside a div</a>"</pml>
    <div>
        <pml>
            pml = "<p>In a div inside a div</p>"
        </pml>
    </div>
</div>
<ul>
    <li>
        <pml>pml = "\t<p>\ttabs work as well.</p>"</pml>
        <pml>pml = "\t<p>     and spaces too!.</p>"</pml>
    </li>
    <li>
        <pml>
            pml = "\t<small>It's a small world after all</small>"
        </pml>
    </li>
        <pml>
            pml = "\t<small>It's a small world after all</small>"
        </pml>
    </li>
        <pml>
            pml = "\t<small>It's a small world after all</small>"
        </pml>
    </li>
        <pml>
            pml = "\t<small>It's a small world after all</small>"
        </pml>
    </li>
        <pml>
            pml = "{} is accessible anywhere in the script.".format( hello_again() )
        </pml>
    </li>
</ul>
<pml>
    pml = "\tThat's about it.  Thanks for your time!"
</pml>
</html>