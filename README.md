# todoist_tests

Setup steps.
1. Python setup:
1.1. Install Python 3.6
1.2. Clone or download repo
1.3. From todoist_tests folder run (to install python libraries) 
```
pip install -r requirements.txt 
```

2. Appium setup:
2.1. Install npm 
```
brew install node
```
2.2. Install appium and appium doctor
```
npm install -g appium
npm install -g appium_doctor
```
2.3. For using Appium we need to install latest JDK 8 
You can download latest JDK by [link](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
2.4. Download all the Android SDK necessary tools, that includes mandatorily platform-tools and build-tools [link](https://developer.android.com/studio/index.html)
2.4. In your bash add the following path using following format:
```
export ANDROID_HOME=/Users/username/Library/Android/sdk .  (copy it from the sdk manager in android studio)
export PATH=$ANDROID_HOME/platform-tools:$PATH
export PATH=$ANDROID_HOME/tools:$PATH
export JAVA_HOME=$(/usr/libexec/java_home)export       PATH="/usr/local/opt/openssl/bin:$PATH"
```
