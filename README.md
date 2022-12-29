# lomiri-specs
Lomiri/Unity8 RPM spec files for Fedora
**Currently this fails with:**
```
(process:15757): GLib-GIO-ERROR **: 20:57:15.067: Settings schema 'com.lomiri.keyboard.maliit' is not installed
Trace/breakpoint trap
```

##Lomiri RPM list:
### Core Packages
* [X] lomiri
* [X] lomiri-api
* [X] qtmir
* [X] click
* [X] lomiri-app-launch
* [X] dbus-test-runner
* [X] lomiri-mir
* [X] apparmor
* [X] lomiri-url-dispatcher
* [X] process-cpp
* [X] lomiri-ui-toolkit
* [X] qt5-mobility
* [X] qt5-pim
* [X] gsettings-qt
* [X] content-hub
* [X] lomiri-download-manager
* [X] qtdbustest
* [X] qtdbusmock
* [X] geonames
* [X] qmenumodel
* [X] deviceinfo
* [X] lomiri-system-settings
* [X] lomiri-settings-components
* [X] lomiri-indicator-network
* [X] qofono
* [X] lomiri-schemas
* [X] gmenuharness
* [X] libusermetrics
* [X] qdjango
* [] lomiri-keyboard
* [] maliit-framework

### Core App Packages
* [] lomiri-terminal-app
* [] lomiri-filemanager-app
* [] lomiri-clock-app
* [] lomiri-calculator-app
* [] lomiri-gallery-app
* [] lomiri-music-app
* [] ubports-app
* [] lomiri-docviewer-app
* [] lomiri-notes-app
* [] lomiri-camera-app
* [] morph-browser

### Extra Functionality for Lomiri
* [X] lomiri-system-compositor
* [] ubuntu-touch-session
* [X] lomiri-desktop-session
* [X] suru-icon-theme
* [] ubuntu-sdk
* [] Extra functionality for lomiri-system-settings
	* [] lomiri-system-settings-*
	* [] ayatana-indicator-datetime

## Thanks To
* [lomiri-on-fedora](https://gitlab.com/erlend.io/lomiri-on-fedora) for examples on how to build some RPMs