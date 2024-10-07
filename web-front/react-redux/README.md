# react redux

Revoyons brièvement la différence entre les props et le state, ce qu’ils nous permettent de faire et leurs limites.

En réutilisant nos composants, nous souhaitons la plupart du temps adapter leur comportement selon leur emplacement dans l’application ou selon certaines données provenant du composant parent. Nous utilisons donc à cet effet les props, qui seront appliqués à nos composants.

```javascript
const IMAGES = [
{
    url: "https://unsplash.com/fr/photos/cjSUZMA2iW8",
    title: "Un cheval"
},
{
    url: "https://unsplash.com/fr/photos/1ZjI3KgB9Co",
    title: "Un chien"
}
]


const Container = () => {
    return IMAGES.map((image, index) => <Picture url={image.url} title={image.title} key={index} />
}
```

Le state, ou état local du composant, nous permet de stocker à l’échelle de notre composant des valeurs qui changent et dont les changements ont une incidence sur le comportement de notre composant :

```javascript
const Counter = () => {
    const [count, setCount] = useState(0)

    return <div>
        <span>Valeur du compteur: {count}</span>
        <button onClick={() => setCount(count + 1)}>ajouter</button>
    </div>
}
```

En combinant props et state, il nous est donc possible de partager des valeurs de states entre des composants faisant partie de la même branche, c'est-à-dire ayant un parent commun.

Pour accéder au state d’un parent, un composant doit recevoir en props les valeurs du state du parent. Un composant peut modifier le state de son parent si celui-ci obtient la méthode setState  , qui permet de modifier le state en props. On dit que les props descendent et que l’état remonte

Notez aussi qu’un composant A qui partage le même parent que le composant B ne peut pas accéder au state de celui-ci. C’est une contrainte, puisque faire remonter le state dans le composant parent devient ici l’unique moyen de partager le state entre A et B.

À l’image d’une étagère remplie de livres dans lesquels des élèves se servent au moment voulu, peut-on imaginer stocker les données à un seul endroit et connecter chaque composant qui aurait besoin de ceux-ci ?

C’est ce que propose Dan Abramov via la librairie Redux qui s’inspire de l’architecture Flux.

Le principe de l’architecture flux est le suivant :

nous stockons un état général dans ce qu’on appelle des stores ;

les composants qui ont besoin d’une valeur de ce state viennent consulter le store et s’abonner aux changements de ce state ;

le store possède un mécanisme qui à chaque changement du state, va informer chaque composant abonné qu’un changement a eu lieu ;

chaque composant peut alors relire le contenu du state et mettre à jour son état local.

Les boîtes représentent les composants. Ici, nous visualisons la distribution d’un state A en tant que props A et B dans les composant A et B.
L'état centralisé simplifie la distribution d'état dans l'application React
Ainsi nous stockons l’état à l’extérieur de notre application qui vient s’alimenter le moment voulu.



## Installing dependencies

You will need Node, the React Native command line interface, a JDK, and Android Studio.

While you can use any editor of your choice to develop your app, you will need to install Android Studio in order to set up the necessary tooling to build your React Native app for Android.

## Node

Follow the installation instructions for your Linux distribution to install Node 18.18 or newer.

## Java Development Kit

React Native currently recommends version 17 of the Java SE Development Kit (JDK). You may encounter problems using higher JDK versions. You may download and install OpenJDK from AdoptOpenJDK or your system packager.

## Android development environment

Setting up your development environment can be somewhat tedious if you're new to Android development. If you're already familiar with Android development, there are a few things you may need to configure. In either case, please make sure to carefully follow the next few steps.

1. Install Android Studio
Download and install Android Studio. While on Android Studio installation wizard, make sure the boxes next to all of the following items are checked:

* Android SDK
* Android SDK Platform
* Android Virtual Device

Then, click "Next" to install all of these components.

If the checkboxes are grayed out, you will have a chance to install these components later on.

Once setup has finalized and you're presented with the Welcome screen, proceed to the next step.

2. Install the Android SDK

Android Studio installs the latest Android SDK by default. Building a React Native app with native code, however, requires the Android 14 (UpsideDownCake) SDK in particular. Additional Android SDKs can be installed through the SDK Manager in Android Studio.

To do that, open Android Studio, click on "Configure" button and select "SDK Manager".

The SDK Manager can also be found within the Android Studio "Settings" dialog, under Languages & Frameworks → Android SDK.

Select the "SDK Platforms" tab from within the SDK Manager, then check the box next to "Show Package Details" in the bottom right corner. Look for and expand the Android 14 (UpsideDownCake) entry, then make sure the following items are checked:

* Android SDK Platform 34
* Intel x86 Atom_64 System Image or Google APIs Intel x86 Atom System Image

Next, select the "SDK Tools" tab and check the box next to "Show Package Details" here as well. Look for and expand the "Android SDK Build-Tools" entry, then make sure that 34.0.0 is selected.

Finally, click "Apply" to download and install the Android SDK and related build tools.

3. Configure the ANDROID_HOME environment variable

The React Native tools require some environment variables to be set up in order to build apps with native code.

Add the following lines to your $HOME/.bash_profile or $HOME/.bashrc (if you are using zsh then ~/.zprofile or ~/.zshrc) config file:

```bash
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

.bash_profile is specific to bash. If you're using another shell, you will need to edit the appropriate shell-specific config file.

Type source $HOME/.bash_profile for bash or source $HOME/.zprofile to load the config into your current shell. Verify that ANDROID_HOME has been set by running echo $ANDROID_HOME and the appropriate directories have been added to your path by running echo $PATH.

Please make sure you use the correct Android SDK path. You can find the actual location of the SDK in the Android Studio "Settings" dialog, under Languages & Frameworks → Android SDK.

## Watchman

Follow the Watchman installation guide to compile and install Watchman from source.

Watchman is a tool by Facebook for watching changes in the filesystem. It is highly recommended you install it for better performance and increased compatibility in certain edge cases (translation: you may be able to get by without installing this, but your mileage may vary; installing this now may save you from a headache later).

## Preparing the Android device

You will need an Android device to run your React Native Android app. This can be either a physical Android device, or more commonly, you can use an Android Virtual Device which allows you to emulate an Android device on your computer.

Either way, you will need to prepare the device to run Android apps for development.

## Using a physical device

If you have a physical Android device, you can use it for development in place of an AVD by plugging it in to your computer using a USB cable and following the instructions here.

## Using a virtual device

If you use Android Studio to open ./AwesomeProject/android, you can see the list of available Android Virtual Devices (AVDs) by opening the "AVD Manager" from within Android Studio. Look for an icon that looks like this:

## Android Studio AVD Manager

If you have recently installed Android Studio, you will likely need to create a new AVD. Select "Create Virtual Device...", then pick any Phone from the list and click "Next", then select the UpsideDownCake API Level 34 image.

We recommend configuring VM acceleration on your system to improve performance. Once you've followed those instructions, go back to the AVD Manager.

Click "Next" then "Finish" to create your AVD. At this point you should be able to click on the green triangle button next to your AVD to launch it.

That's it!

## Integration with Existing Apps

React Native is great when you are starting a new mobile app from scratch. However, it also works well for adding a single view or user flow to existing native applications. With a few steps, you can add new React Native based features, screens, views, etc.

The specific steps are different depending on what platform you're targeting.

## Key Concepts

The keys to integrating React Native components into your Android application are to:

* Set up React Native dependencies and directory structure.
* Develop your React Native components in JavaScript.
* Add a ReactRootView to your Android app. This view will serve as the container for your React Native component.
* Start the React Native server and run your native application.
* Verify that the React Native aspect of your application works as expected.

## Prerequisites

Follow the guide on setting up your development environment to configure your development environment for building React Native apps for Android.

1. Set up directory structure
To ensure a smooth experience, create a new folder for your integrated React Native project, then copy your existing Android project to an /android subfolder.

2. Install JavaScript dependencies
Go to the root directory for your project and create a new package.json file with the following contents:

```javascript
{
  "name": "MyReactNativeApp",
  "version": "0.0.1",
  "private": true,
  "scripts": {
    "start": "react-native start"
  }
}
```

Next, install the react and react-native packages. Open a terminal or command prompt, then navigate to the directory with your package.json file and run:

```bash
npm install react-native
```

This will print a message similar to the following (scroll up in the installation command output to see it):

warning "react-native@0.70.5" has unmet peer dependency "react@18.1.0"

This is OK, it means we also need to install React:

```bash
npm install react@version_printed_above
```

Installation process has created a new /node_modules folder. This folder stores all the JavaScript dependencies required to build your project.

Add node_modules/ to your .gitignore file.

## Adding React Native to your app

### Configuring Gradle

React Native uses the React Native Gradle Plugin to configure your dependencies and project setup.

First, let's edit your settings.gradle file by adding this line:

```javascript
includeBuild('../node_modules/@react-native/gradle-plugin')
```

Then you need to open your top level build.gradle and include this line:

```javascript
buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath("com.android.tools.build:gradle:7.3.1")
+       classpath("com.facebook.react:react-native-gradle-plugin")
    }
}
```

This makes sure the React Native Gradle Plugin is available inside your project. Finally, add those lines inside your app's build.gradle file (it's a different build.gradle file inside your app folder):

```javascript
apply plugin: "com.android.application"
+apply plugin: "com.facebook.react"

repositories {
    mavenCentral()
}

dependencies {
    // Other dependencies here
+   implementation "com.facebook.react:react-android"
+   implementation "com.facebook.react:hermes-android"
}
```

Those dependencies are available on mavenCentral() so make sure you have it defined in your repositories{} block.

info
We intentionally don't specify the version for those implementation dependencies as the React Native Gradle Plugin will take care of it. If you don't use the React Native Gradle Plugin, you'll have to specify version manually.

Enable native modules autolinking
To use the power of autolinking, we have to apply it a few places. First add the following entry to settings.gradle:

apply from: file("../node_modules/@react-native-community/cli-platform-android/native_modules.gradle"); applyNativeModulesSettingsGradle(settings)


Next add the following entry at the very bottom of the app/build.gradle:

apply from: file("../../node_modules/@react-native-community/cli-platform-android/native_modules.gradle"); applyNativeModulesAppBuildGradle(project)


Configuring permissions
Next, make sure you have the Internet permission in your AndroidManifest.xml:

<uses-permission android:name="android.permission.INTERNET" />

If you need to access to the DevSettingsActivity add to your AndroidManifest.xml:

<activity android:name="com.facebook.react.devsupport.DevSettingsActivity" />

This is only used in dev mode when reloading JavaScript from the development server, so you can strip this in release builds if you need to.

Cleartext Traffic (API level 28+)
Starting with Android 9 (API level 28), cleartext traffic is disabled by default; this prevents your application from connecting to the Metro bundler. The changes below allow cleartext traffic in debug builds.

1. Apply the usesCleartextTraffic option to your Debug AndroidManifest.xml
<!-- ... -->
<application
  android:usesCleartextTraffic="true" tools:targetApi="28" >
  <!-- ... -->
</application>
<!-- ... -->

This is not required for Release builds.

To learn more about Network Security Config and the cleartext traffic policy see this link.

Code integration
Now we will actually modify the native Android application to integrate React Native.

The React Native component
The first bit of code we will write is the actual React Native code for the new "High Score" screen that will be integrated into our application.

1. Create a index.js file
First, create an empty index.js file in the root of your React Native project.

index.js is the starting point for React Native applications, and it is always required. It can be a small file that requires other file that are part of your React Native component or application, or it can contain all the code that is needed for it. In our case, we will put everything in index.js.

2. Add your React Native code
In your index.js, create your component. In our sample here, we will add a <Text> component within a styled <View>:

import React from 'react';
import {AppRegistry, StyleSheet, Text, View} from 'react-native';

const HelloWorld = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.hello}>Hello, World</Text>
    </View>
  );
};
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
  },
  hello: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
});

AppRegistry.registerComponent(
  'MyReactNativeApp',
  () => HelloWorld,
);

3. Configure permissions for development error overlay
If your app is targeting the Android API level 23 or greater, make sure you have the permission android.permission.SYSTEM_ALERT_WINDOW enabled for the development build. You can check this with Settings.canDrawOverlays(this);. This is required in dev builds because React Native development errors must be displayed above all the other windows. Due to the new permissions system introduced in the API level 23 (Android M), the user needs to approve it. This can be achieved by adding the following code to your Activity's in onCreate() method.

private final int OVERLAY_PERMISSION_REQ_CODE = 1;  // Choose any value

...

if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
    if (!Settings.canDrawOverlays(this)) {
        Intent intent = new Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
                                   Uri.parse("package:" + getPackageName()));
        startActivityForResult(intent, OVERLAY_PERMISSION_REQ_CODE);
    }
}

Finally, the onActivityResult() method (as shown in the code below) has to be overridden to handle the permission Accepted or Denied cases for consistent UX. Also, for integrating Native Modules which use startActivityForResult, we need to pass the result to the onActivityResult method of our ReactInstanceManager instance.

@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    if (requestCode == OVERLAY_PERMISSION_REQ_CODE) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            if (!Settings.canDrawOverlays(this)) {
                // SYSTEM_ALERT_WINDOW permission not granted
            }
        }
    }
    mReactInstanceManager.onActivityResult( this, requestCode, resultCode, data );
}

The Magic: ReactRootView
Let's add some native code in order to start the React Native runtime and tell it to render our JS component. To do this, we're going to create an Activity that creates a ReactRootView, starts a React application inside it and sets it as the main content view.

If you are targeting Android version <5, use the AppCompatActivity class from the com.android.support:appcompat package instead of Activity.

public class MyReactActivity extends Activity implements DefaultHardwareBackBtnHandler {
    private ReactRootView mReactRootView;
    private ReactInstanceManager mReactInstanceManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        SoLoader.init(this, false);

        mReactRootView = new ReactRootView(this);
        List<ReactPackage> packages = new PackageList(getApplication()).getPackages();
        // Packages that cannot be autolinked yet can be added manually here, for example:
        // packages.add(new MyReactNativePackage());
        // Remember to include them in `settings.gradle` and `app/build.gradle` too.

        mReactInstanceManager = ReactInstanceManager.builder()
                .setApplication(getApplication())
                .setCurrentActivity(this)
                .setBundleAssetName("index.android.bundle")
                .setJSMainModulePath("index")
                .addPackages(packages)
                .setUseDeveloperSupport(BuildConfig.DEBUG)
                .setInitialLifecycleState(LifecycleState.RESUMED)
                .build();
        // The string here (e.g. "MyReactNativeApp") has to match
        // the string in AppRegistry.registerComponent() in index.js
        mReactRootView.startReactApplication(mReactInstanceManager, "MyReactNativeApp", null);

        setContentView(mReactRootView);
    }

    @Override
    public void invokeDefaultOnBackPressed() {
        super.onBackPressed();
    }
}

If you are using a starter kit for React Native, replace the "HelloWorld" string with the one in your index.js file (it’s the first argument to the AppRegistry.registerComponent() method).

Perform a “Sync Project files with Gradle” operation.

If you are using Android Studio, use Alt + Enter to add all missing imports in your MyReactActivity class. Be careful to use your package’s BuildConfig and not the one from the facebook package.

We need set the theme of MyReactActivity to Theme.AppCompat.Light.NoActionBar because some React Native UI components rely on this theme.

<activity
  android:name=".MyReactActivity"
  android:label="@string/app_name"
  android:theme="@style/Theme.AppCompat.Light.NoActionBar">
</activity>

A ReactInstanceManager can be shared by multiple activities and/or fragments. You will want to make your own ReactFragment or ReactActivity and have a singleton holder that holds a ReactInstanceManager. When you need the ReactInstanceManager (e.g., to hook up the ReactInstanceManager to the lifecycle of those Activities or Fragments) use the one provided by the singleton.

Next, we need to pass some activity lifecycle callbacks to the ReactInstanceManager and ReactRootView:

@Override
protected void onPause() {
    super.onPause();

    if (mReactInstanceManager != null) {
        mReactInstanceManager.onHostPause(this);
    }
}

@Override
protected void onResume() {
    super.onResume();

    if (mReactInstanceManager != null) {
        mReactInstanceManager.onHostResume(this, this);
    }
}

@Override
protected void onDestroy() {
    super.onDestroy();

    if (mReactInstanceManager != null) {
        mReactInstanceManager.onHostDestroy(this);
    }
    if (mReactRootView != null) {
        mReactRootView.unmountReactApplication();
    }
}

We also need to pass back button events to React Native:

@Override
 public void onBackPressed() {
    if (mReactInstanceManager != null) {
        mReactInstanceManager.onBackPressed();
    } else {
        super.onBackPressed();
    }
}

This allows JavaScript to control what happens when the user presses the hardware back button (e.g. to implement navigation). When JavaScript doesn't handle the back button press, your invokeDefaultOnBackPressed method will be called. By default this finishes your Activity.

Finally, we need to hook up the dev menu. By default, this is activated by (rage) shaking the device, but this is not very useful in emulators. So we make it show when you press the hardware menu button (use Ctrl + M if you're using Android Studio emulator):

@Override
public boolean onKeyUp(int keyCode, KeyEvent event) {
    if (keyCode == KeyEvent.KEYCODE_MENU && mReactInstanceManager != null) {
        mReactInstanceManager.showDevOptionsDialog();
        return true;
    }
    return super.onKeyUp(keyCode, event);
}

Now your activity is ready to run some JavaScript code.

Test your integration
You have now done all the basic steps to integrate React Native with your current application. Now we will start the Metro bundler to build the index.bundle package and the server running on localhost to serve it.

1. Run the packager
To run your app, you need to first start the development server. To do this, run the following command in the root directory of your React Native project:

npm start

2. Run the app
Now build and run your Android app as normal.

Once you reach your React-powered activity inside the app, it should load the JavaScript code from the development server and display:

Screenshot

Creating a release build in Android Studio
You can use Android Studio to create your release builds too! It’s as quick as creating release builds of your previously-existing native Android app.

If you use the React Native Gradle Plugin as described above, everything should work when running app from Android Studio.

If you're not using the React Native Gradle Plugin, there’s one additional step which you’ll have to do before every release build. You need to execute the following to create a React Native bundle, which will be included with your native Android app:

$ npx react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/com/your-company-name/app-package-name/src/main/assets/index.android.bundle --assets-dest android/com/your-company-name/app-package-name/src/main/res/


Don’t forget to replace the paths with correct ones and create the assets folder if it doesn’t exist.

Now, create a release build of your native app from within Android Studio as usual and you should be good to go!

Now what?
At this point you can continue developing your app as usual. Refer to our debugging and deployment docs to learn more about working with React Native.

Integration with an Android Fragment
The guide for Integration with Existing Apps details how to integrate a full-screen React Native app into an existing Android app as an Activity. To use React Native components within Fragments in an existing app requires some additional setup. The benefit of this is that it allows for a native app to integrate React Native components alongside native fragments in an Activity.

1. Add React Native to your app
Follow the guide for Integration with Existing Apps until the Code integration section. Continue to follow Step 1. Create an index.android.js file and Step 2. Add your React Native code from this section.

2. Integrating your App with a React Native Fragment
You can render your React Native component into a Fragment instead of a full screen React Native Activity. The component may be termed a "screen" or "fragment" and it will function in the same manner as an Android fragment, likely containing child components. These components can be placed in a /fragments folder and the child components used to compose the fragment can be placed in a /components folder.

You will need to implement the ReactApplication interface in your main Application Java/Kotlin class. If you have created a new project from Android Studio with a default activity, you will need to create a new class (e.g. MyReactApplication.java or MyReactApplication.kt). If it is an existing class you can find this main class in your AndroidManifest.xml file. Under the <application /> tag you should see a property android:name e.g. android:name=".MyReactApplication". This value is the class you want to implement and provide the required methods to.

Ensure your main Application class implements ReactApplication:

class MyReactApplication: Application(), ReactApplication {...}

Override the required methods getUseDeveloperSupport, getPackages and getReactNativeHost:

class MyReactApplication : Application(), ReactApplication {
    override fun onCreate() {
        super.onCreate()
        SoLoader.init(this, false)
    }
    private val reactNativeHost =
        object : DefaultReactNativeHost(this) {
            override fun getUseDeveloperSupport() = BuildConfig.DEBUG
            override fun getPackages(): List<ReactPackage> {
                val packages = PackageList(this).getPackages().toMutableList()
                // Packages that cannot be autolinked yet can be added manually here
                return packages
            }
        }
    override fun getReactNativeHost(): ReactNativeHost = reactNativeHost
}

If you are using Android Studio, use Alt + Enter to add all missing imports in your class. Alternatively these are the required imports to include manually:

import android.app.Application

import com.facebook.react.PackageList
import com.facebook.react.ReactApplication
import com.facebook.react.ReactNativeHost
import com.facebook.react.ReactPackage
import com.facebook.react.defaults.DefaultReactNativeHost
import com.facebook.soloader.SoLoader

Perform a "Sync Project files with Gradle" operation.

Step 3. Add a FrameLayout for the React Native Fragment
You will now add your React Native Fragment to an Activity. For a new project this Activity will be MainActivity but it could be any Activity and more fragments can be added to additional Activities as you integrate more React Native components into your app.

First add the React Native Fragment to your Activity's layout. For example main_activity.xml in the res/layouts folder.

Add a <FrameLayout> with an id, width and height. This is the layout you will find and render your React Native Fragment into.

<FrameLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/reactNativeFragment"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />

Step 4. Add a React Native Fragment to the FrameLayout
To add your React Native Fragment to your layout you need to have an Activity. As mentioned in a new project this will be MainActivity. In this Activity add a button and an event listener. On button click you will render your React Native Fragment.

Modify your Activity layout to add the button:

<Button
    android:layout_margin="10dp"
    android:id="@+id/button"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Show react fragment" />

Now in your Activity class (e.g. MainActivity.java or MainActivity.kt) you need to add an OnClickListener for the button, instantiate your ReactFragment and add it to the frame layout.

Add the button field to the top of your Activity:

private lateinit var button: Button

Update your Activity's onCreate method as follows:

override fun onCreate(savedInstanceState: Bundle) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.main_activity)
    button = findViewById<Button>(R.id.button)
    button.setOnClickListener {
        val reactNativeFragment = ReactFragment.Builder()
                .setComponentName("HelloWorld")
                .setLaunchOptions(getLaunchOptions("test message"))
                .build()
        getSupportFragmentManager()
                .beginTransaction()
                .add(R.id.reactNativeFragment, reactNativeFragment)
                .commit()
    }
}

In the code above Fragment reactNativeFragment = new ReactFragment.Builder() creates the ReactFragment and getSupportFragmentManager().beginTransaction().add() adds the Fragment to the Frame Layout.

If you are using a starter kit for React Native, replace the "HelloWorld" string with the one in your index.js or index.android.js file (it’s the first argument to the AppRegistry.registerComponent() method).

Add the getLaunchOptions method which will allow you to pass props through to your component. This is optional and you can remove setLaunchOptions if you don't need to pass any props.

private fun getLaunchOptions(message: String) = Bundle().apply {
    putString("message", message)
}


Add all missing imports in your Activity class. Be careful to use your package’s BuildConfig and not the one from the facebook package! Alternatively these are the required imports to include manually:

import android.app.Application

import com.facebook.react.ReactApplication
import com.facebook.react.ReactNativeHost
import com.facebook.react.ReactPackage
import com.facebook.react.shell.MainReactPackage
import com.facebook.soloader.SoLoader


Perform a "Sync Project files with Gradle" operation.

Step 5. Test your integration
Make sure you run yarn to install your react-native dependencies and run yarn native to start the metro bundler. Run your android app in Android Studio and it should load the JavaScript code from the development server and display it in your React Native Fragment in the Activity.

Step 6. Additional setup - Native modules
You may need to call out to existing Java/Kotlin code from your react component. Native modules allow you to call out to native code and run methods in your native app. Follow the setup here native-modules-android

Building For TV Devices
TV devices support has been implemented with the intention of making existing React Native applications work on Apple TV and Android TV, with few or no changes needed in the JavaScript code for the applications.

Deprecated. TV support has moved to the React Native for TV repository.

Build changes
Native layer: To run React Native project on Android TV make sure to make the following changes to AndroidManifest.xml
  <!-- Add custom banner image to display as Android TV launcher icon -->
 <application
  ...
  android:banner="@drawable/tv_banner"
  >
    ...
    <intent-filter>
      ...
      <!-- Needed to properly create a launch intent when running on Android TV -->
      <category android:name="android.intent.category.LEANBACK_LAUNCHER"/>
    </intent-filter>
    ...
  </application>

JavaScript layer: Support for Android TV has been added to Platform.android.js. You can check whether code is running on Android TV by doing
const Platform = require('Platform');
const running_on_android_tv = Platform.isTV;

Code changes
Access to touchable controls: When running on Android TV the Android framework will automatically apply a directional navigation scheme based on relative position of focusable elements in your views. The Touchable mixin has code added to detect focus changes and use existing methods to style the components properly and initiate the proper actions when the view is selected using the TV remote, so TouchableWithoutFeedback, TouchableHighlight, TouchableOpacity and TouchableNativeFeedback will work as expected. In particular:

onFocus will be executed when the touchable view goes into focus
onBlur will be executed when the touchable view goes out of focus
onPress will be executed when the touchable view is actually selected by pressing the "select" button on the TV remote.
TV remote/keyboard input: A new native class, ReactAndroidTVRootViewHelper, sets up key events handlers for TV remote events. When TV remote events occur, this class fires a JS event. This event will be picked up by instances of the TVEventHandler JavaScript object. Application code that needs to implement custom handling of TV remote events can create an instance of TVEventHandler and listen for these events, as in the following code:

const TVEventHandler = require('TVEventHandler');

class Game2048 extends React.Component {
  _tvEventHandler: any;

  _enableTVEventHandler() {
    this._tvEventHandler = new TVEventHandler();
    this._tvEventHandler.enable(this, function (cmp, evt) {
      if (evt && evt.eventType === 'right') {
        cmp.setState({board: cmp.state.board.move(2)});
      } else if (evt && evt.eventType === 'up') {
        cmp.setState({board: cmp.state.board.move(1)});
      } else if (evt && evt.eventType === 'left') {
        cmp.setState({board: cmp.state.board.move(0)});
      } else if (evt && evt.eventType === 'down') {
        cmp.setState({board: cmp.state.board.move(3)});
      } else if (evt && evt.eventType === 'playPause') {
        cmp.restartGame();
      }
    });
  }

  _disableTVEventHandler() {
    if (this._tvEventHandler) {
      this._tvEventHandler.disable();
      delete this._tvEventHandler;
    }
  }

  componentDidMount() {
    this._enableTVEventHandler();
  }

  componentWillUnmount() {
    this._disableTVEventHandler();
  }
}

Dev Menu support: On the emulator, cmd-M will bring up the Dev Menu, similar to Android. To bring it up on a real Android TV device, press the menu button or long press the fast-forward button on the remote. (Please do not shake the Android TV device, that will not work :) )

Known issues:

TextInput components do not work for now (i.e. they cannot receive focus automatically, see this comment).
It is however possible to use a ref to manually trigger inputRef.current.focus().
You can wrap your input inside a TouchableWithoutFeedback component and trigger focus in the onFocus event of that touchable. This enables opening the keyboard via the arrow keys.
The keyboard might reset its state after each keypress (this might only happen inside the Android TV emulator).
The content of Modal components cannot receive focus, see this issue for details.

Creating your own React Native platform
Right now the process of creating a React Native platform from scratch is not very well documented - one of the goals of the upcoming re-architecture (Fabric) is to make maintaining a platform easier.

Bundling
As of React Native 0.57 you can now register your React Native platform with React Native's JavaScript bundler, Metro. This means you can pass --platform example to npx react-native bundle, and it will look for JavaScript files with the .example.js suffix.

To register your platform with RNPM, your module's name must match one of these patterns:

react-native-example - It will search all top-level modules that start with react-native-
@org/react-native-example - It will search for modules that start with react-native- under any scope
@react-native-example/module - It will search in all modules under scopes with names starting with @react-native-
You must also have an entry in your package.json like this:

{
  "rnpm": {
    "haste": {
      "providesModuleNodeModules": ["react-native-example"],
      "platforms": ["example"]
    }
  }
}

"providesModuleNodeModules" is an array of modules that will get added to the Haste module search path, and "platforms" is an array of platform suffixes that will be added as valid platforms.

Running On Device
It's always a good idea to test your app on an actual device before releasing it to your users. This document will guide you through the necessary steps to run your React Native app on a device and to get it ready for production.

info
If you used create-expo-app to set up your project, you can run your app on a device in Expo Go by scanning the QR code that is displayed when you run npm start. Refer to the Expo guide for running your project on your device for more information.

Running your app on Android devices
Development OS
1. Enable Debugging over USB
Most Android devices can only install and run apps downloaded from Google Play, by default. You will need to enable USB Debugging on your device in order to install your app during development.

To enable USB debugging on your device, you will first need to enable the "Developer options" menu by going to Settings → About phone → Software information and then tapping the Build number row at the bottom seven times. You can then go back to Settings → Developer options to enable "USB debugging".

2. Plug in your device via USB
Let's now set up an Android device to run our React Native projects. Go ahead and plug in your device via USB to your development machine.

Next, check the manufacturer code by using lsusb (on mac, you must first install lsusb). lsusb should output something like this:

$ lsusb
Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 003: ID 22b8:2e76 Motorola PCS
Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

These lines represent the USB devices currently connected to your machine.

You want the line that represents your phone. If you're in doubt, try unplugging your phone and running the command again:

$ lsusb
Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

You'll see that after removing the phone, the line which has the phone model ("Motorola PCS" in this case) disappeared from the list. This is the line that we care about.

Bus 001 Device 003: ID 22b8:2e76 Motorola PCS

From the above line, you want to grab the first four digits from the device ID:

22b8:2e76

In this case, it's 22b8. That's the identifier for Motorola.

You'll need to input this into your udev rules in order to get up and running:

echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="22b8", MODE="0666", GROUP="plugdev"' | sudo tee /etc/udev/rules.d/51-android-usb.rules


Make sure that you replace 22b8 with the identifier you get in the above command.

Now check that your device is properly connecting to ADB, the Android Debug Bridge, by running adb devices.

$ adb devices
List of devices attached
emulator-5554 offline   # Google emulator
14ed2fcc device         # Physical device

Seeing device in the right column means the device is connected. You must have only one device connected at a time.

3. Run your app
From the root of your project, type the following in your command prompt to install and launch your app on the device:

npm run android

If you get a "bridge configuration isn't available" error, see Using adb reverse.

Hint: You can also use the React Native CLI to generate and run a release build (e.g. from the root of your project: yarn android --mode release).

Connecting to the development server
You can also iterate quickly on a device by connecting to the development server running on your development machine. There are several ways of accomplishing this, depending on whether you have access to a USB cable or a Wi-Fi network.

Method 1: Using adb reverse (recommended)
You can use this method if your device is running Android 5.0 (Lollipop) or newer, it has USB debugging enabled, and it is connected via USB to your development machine.

Run the following in a command prompt:

$ adb -s <device name> reverse tcp:8081 tcp:8081

To find the device name, run the following adb command:

$ adb devices

You can now enable Live reloading from the Dev Menu. Your app will reload whenever your JavaScript code has changed.

Method 2: Connect via Wi-Fi
You can also connect to the development server over Wi-Fi. You'll first need to install the app on your device using a USB cable, but once that has been done you can debug wirelessly by following these instructions. You'll need your development machine's current IP address before proceeding.

Open a terminal and type /sbin/ifconfig to find your machine's IP address.

Make sure your laptop and your phone are on the same Wi-Fi network.
Open your React Native app on your device.
You'll see a red screen with an error. This is OK. The following steps will fix that.
Open the in-app Dev Menu.
Go to Dev Settings → Debug server host & port for device.
Type in your machine's IP address and the port of the local dev server (e.g. 10.0.1.1:8081).
Go back to the Dev Menu and select Reload JS.
You can now enable Live reloading from the Dev Menu. Your app will reload whenever your JavaScript code has changed.

Building your app for production
You have built a great app using React Native, and you are now itching to release it in the Play Store. The process is the same as any other native Android app, with some additional considerations to take into account. Follow the guide for generating a signed APK to learn more.

