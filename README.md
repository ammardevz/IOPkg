<h1>IOPkg - Open source Platform-Independent Package Manager</h1>

<p>IOPkg is a Python-based open-source package manager that allows you to create and manage platform-independent packages. It provides a command-line interface (CLI) for creating, extracting, and inspecting packages.</p>

<h2>Installation</h2>

<p>You can download the latest release of IOPkg from the <a href="https://github.com/ammardevz/IOPkg/releases">GitHub release page</a>. Choose the appropriate release for your platform and download the source code as a ZIP or TAR.GZ archive.</p>

<p>Alternatively, you can clone the repository and build it from source:</p>

<pre><code>git clone https://github.com/ammardevz/IOPkg.git
cd IOPkg
python packager.py --help
</code></pre>

<h2>Usage</h2>

<h3>Creating a Package</h3>

<p>To create a package, use the <code>create</code> command. Provide a name for the package and specify the files and directories to include.</p>

<pre><code>python packager.py create &lt;package_name&gt; --include &lt;file_or_directory_path&gt;
</code></pre>

<p>Example:</p>

<pre><code>python packager.py create my_package --include src/
</code></pre>

<p>This will create a package named <code>my_package.iopkg</code> that includes all the files and directories within the <code>src/</code> directory.</p>

<h3>Extracting Package Information</h3>

<p>To extract information from a package, use the <code>info</code> command. Provide the name of the package file.</p>

<pre><code>python packager.py info &lt;package_name&gt;
</code></pre>

<p>Example:</p>

<pre><code>python packager.py info my_package.iopkg
</code></pre>

<p>This will display information about the package, including the author, creation date, version, and the list of files included in the package.</p>

<h3>Unpacking a Package</h3>

<p>To unpack a package and extract its contents, use the <code>unpack</code> command. Provide the name of the package file and specify the target directory where the contents should be extracted.</p>

<pre><code>python packager.py unpack &lt;package_name&gt; --target &lt;target_directory&gt;
</code></pre>

<p>Example:</p>

<pre><code>python packager.py unpack my_package.iopkg --target ./output/
</code></pre>

<p>This will extract the contents of the package <code>my_package.iopkg</code> to the <code>output/</code> directory.</p>

<h2>Contributing</h2>

<p>Contributions to IOPkg are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the <a href="https://github.com/ammardevz/IOPkg">GitHub repository</a>.</p>

<h2>License</h2>

<p>IOPkg is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more information.</p>
