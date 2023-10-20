<h1>IOPkg - Open Source Platform-Independent Package Manager</h1>

<p>Welcome to IOPkg, an open-source package manager designed to create and manage platform-independent packages. IOPkg provides a powerful command-line interface (CLI) for package creation, extraction, and inspection.</p>

<h2>Installation</h2>

<p>Get started with IOPkg by downloading the latest release from the official <a href="https://github.com/ammardevz/IOPkg/releases">GitHub release page</a>. Choose the appropriate release for your platform and download the executable file.</p>

<p>Once downloaded, place the `iopkg.exe` file in a directory accessible from the command prompt. This allows you to use IOPkg directly in the command prompt without specifying the Python interpreter.</p>

<h2>Usage</h2>

<h3>Creating a Package</h3>

<p>To create a package, execute the following command:</p>

<pre><code>iopkg create &lt;name&gt; --include &lt;file_or_directory_path&gt;</code></pre>

<p>Arguments:</p>
<ul>
  <li><code>&lt;name&gt;</code>: Specifies the name of the package. The package will be saved as &lt;name&gt;.iopkg.</li>
</ul>

<p>Options:</p>
<ul>
  <li><code>--include, -i</code>: Specifies the list of files and directories to include in the package.</li>
</ul>

<p>Example:</p>

<pre><code>iopkg create my_package --include src/</code></pre>

<p>This command creates a package named <code>my_package.iopkg</code> that includes all files and directories within the <code>src/</code> directory.</p>

<h3>Extracting Package Information</h3>

<p>To extract information from a package, use the following command:</p>

<pre><code>iopkg info &lt;name&gt;</code></pre>

<p>Arguments:</p>
<ul>
  <li><code>&lt;name&gt;</code>: Specifies the name of the package to extract information from.</li>
</ul>

<p>This command displays detailed information about the package, including the author, creation date, version, and the list of files included in the package.</p>

<h3>Unpacking a Package</h3>

<p>To unpack a package and extract its contents, use the following command:</p>

<pre><code>iopkg unpack &lt;name&gt;</code></pre>

<p>Arguments:</p>
<ul>
  <li><code>&lt;name&gt;</code>: Specifies the name of the package to unpack.</li>
</ul>

<p>Example:</p>

<pre><code>iopkg unpack testpkg.iopkg</code></pre>

<p>This command extracts the contents of the package <code>testpkg.iopkg</code> to the current directory.</p>

<h2>Contributing</h2>

<p>We welcome contributions to IOPkg! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the official <a href="https://github.com/ammardevz/IOPkg">GitHub repository</a>.</p>

<h2>License</h2>

<p>IOPkg is licensed under the MIT License. For more information, refer to the <a href="LICENSE">LICENSE</a> file.</p>
