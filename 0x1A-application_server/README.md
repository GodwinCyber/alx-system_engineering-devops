<h1>0x1A. Application server</h1>
DevOps SysAdmin<br>
<p><img src="c7d1ed0a2e10d1b4e9b3.jpg" alt="" loading='lazy' style="" /></p>
<h2>Background Context</h2>
<p>Your web infrastructure is already serving web pages via <code>Nginx</code> that you installed in your <a href="/rltoken/95oRNZ-zRGwLxtWECJqsWA" title="first web stack project" target="_blank">first web stack project</a>. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your <code>Nginx</code> and make is serve your Airbnb clone project.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/B9fOBzIxX_t1289WAuRzJw" title="Application server vs web server" target="_blank">Application server vs web server</a> </li>
<li><a href="/rltoken/kpG6RwmwRJHzRmGUM_ERcA" title="How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04" target="_blank">How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04</a> (As mentioned in the video, do <strong>not</strong> install Gunicorn using <code>virtualenv</code>, just install everything globally)</li>
<li><a href="/rltoken/2LF1j7xKJGYaUtD1HKgUeQ" title="Running Gunicorn" target="_blank">Running Gunicorn</a> </li>
<li><a href="/rltoken/zTCSTQxrH2za4hxbkt8K3g" title="Be careful with the way Flask manages slash" target="_blank">Be careful with the way Flask manages slash</a> in <a href="/rltoken/n5A0nmah-Si78zbNvdb4GA" title="route" target="_blank">route</a>  - <code>strict_slashes</code></li>
<li><a href="/rltoken/cldrneY3Qr7LlDysygzRHw" title="Upstart documentation" target="_blank">Upstart documentation</a> </li>
</ul>

<h2>Requirements</h2>
<h3>General</h3>

<ul>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Everything Python-related must be done using <code>python3</code></li>
<li>All config files must have comments</li>
</ul>

<h3>Bash Scripts</h3>

<ul>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.7-5~ubuntu16.04.1</code> via <code>apt-get</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>
