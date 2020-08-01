# ClickJacking-Bug-Testing
Clickjacking is a malicious technique of tricking a user into clicking on something different from what the user perceives, thus potentially revealing confidential information or allowing others to take control of their computer while clicking on seemingly innocuous objects, including web pages.

<p>This script test if websites are vulnerable to clickjacking attack and creates a POC</p>

<h3>Setup</h3>
<ul>
<li>In command line terminal use : git clone https://github.com/abhinavporwal/ClickJacking-Bug-Testing.git</li>
</ul>

<h3>Example</h3>
<pre> python3 [.py file name] [domain list .txt file] </pre>
<pre> python3 clickjacking.py test.txt </pre>

<h3>Output</h3>
<pre>root@root:~# python3 clickjacking_test.py test.txt

[*] Checking www.google.com

   [-] Website is not vulnerable!

[*] Checking www.facebook.com

   [-] Website is not vulnerable!

[*] Checking www.amazon.com

   [-] Website is not vulnerable!

[*] Checking www.cobaltstrike.com

   [+] Website is vulnerable!
   [*] Created a poc and saved to <URL>.html
</pre>

