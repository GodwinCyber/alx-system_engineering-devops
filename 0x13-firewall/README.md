<h1>0x13. Firewall</h1>
DevOps, SysAdmin,Security
<h2>Concepts</h2>
<em>For this project, we expect you to look at these concepts:</em><br>
<a href="https://intranet.alxswe.com/concepts/68">Web stack debugging</a><br>
<p><img src="284/V1HjQ1Y.png" alt="" loading='lazy' style="" /></p>
<h2>Background Context</h2>

<h3>Your servers without a firewall&hellip;</h3>

<p><img src="holbertonschool-firewall.gif" alt="" loading='lazy' style=""></p>
<h2>Resources</h2>
Read or Watch<br>
<a href="https://en.wikipedia.org/wiki/Firewall_%28computing%29">What is a firewall</a><br>
<h1>More Info</h1>
As explained in the <strong>web stack debugging guide</strong> concept page, telnet is a very good tool to check if sockets are open with telnet IP PORT.<br>
For example, if you want to check if port 22 is open on web-02:<br>
<pre><code>sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is &#39;^]&#39;.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$
</code></pre>

<p>We can see for this example that the connection is successful: 
<code>Connected to web-02.holberton.online.</code></p>

<p>Now let&rsquo;s try connecting to port 2222:</p>

<pre><code>sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$
</code></pre>
<p>We can see that the connection never succeeds, so after some time I just use <code>ctrl+c</code> to kill the process.</p>

<p>This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.</p>

<p>Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on <code>web-01</code>, please perform the test from outside of the school network, like from your <code>web-02</code> server. If you SSH into your <code>web-02</code> server, the traffic will be originating from <code>web-02</code> and not from the school&rsquo;s network, bypassing the firewall.</p>

<h2>Warning!</h2>

<p><strong>Containers on demand cannot be used for this project (Docker container limitation)</strong></p>

<p><strong>Be very careful with firewall rules! For instance, if you ever deny port <code>22/TCP</code> and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.</strong></p>

<h3>General</h3>
<p>
What is HTTPS SSL 2 main roles<br>
What is the purpose encrypting traffic<br>
What SSL termination means<br>
</p>
<h2>Requirements</h2>
<h3>General</h3>
<p>
Allowed editors: vi, vim, emacs<br>
All your files will be interpreted on Ubuntu 16.04 LTS<br>
All your files should end with a new line<br>
A README.md file at the root of the folder of the project is mandatory<br>
All your Bash script files must be executable<br>
Your Bash scripts must pass Shellcheck (version 0.3.7) without any error<br>
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash<br>
The second line of all your Bash scripts should be a comment explaining what is the script doing<br>
</p>
