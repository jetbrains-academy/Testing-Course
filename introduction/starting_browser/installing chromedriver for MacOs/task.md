## Installing the driver for the browser: macOS
When installing Python, you have probably already installed the package manager Homebrew. If not, we recommend doing it now and then with its help installing the program wget for retrieving files from the web.

`brew install wget`

To install the driver, open the site https://sites.google.com/chromium.org/driver/ and copy the link for the ChromeDriver version matching the version of your browser. To find out the browser version, open a new window in Chrome, write chrome://version/ in the search box, and press Enter. In the top line, you'll see the info about the browser's version.

``` 
cd ~/Downloads
wget https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_mac64.zip
```
Unarchive the downloaded file and move it to the `/usr/local/bin` folder, so that it would be globally accessible in your system.

```
unzip chromedriver_mac64.zip
sudo mv chromedriver /usr/local/bin
```
Let's check that the required version of ChromeDriver has been installed.

`chromedriver --version`

The system response should be the following:

`ChromeDriver 76.0.3809.68 (420c9498db8ce8fcd190a954d51297672c1515d5-refs/branch-heads/3809@{#864})`

If you see that, everything is fine and you can proceed to the next step.

However, if you see something like this:

`-bash: chromedriver: command not found`

you need to check if the file chromedriver is in the folder `/usr/local/bin`. If it's not there, run the above commands again. 
