# lomiri-specs
Lomiri/Unity8 RPM spec files for Fedora
**Currently this fails due to other small issues and not being able to login!**
```
lomiri[4073]: [2022-12-30:16:41:32.995] unrecognised option
```

## Lomiri RPM list:
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
* [X] lomiri-keyboard
* [X] ayatana-indicator-datetime
* [X] lomiri-sounds
* [X] libayatana-common
* [X] ayatana-indicator-messages

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
* [] libertine
* [] ubuntu-sdk
* [] Extra functionality for lomiri-system-settings
	* [] lomiri-system-settings-*

## Thanks To
* [lomiri-on-fedora](https://gitlab.com/erlend.io/lomiri-on-fedora) for examples on how to build some RPMs
* [pmaports](https://gitlab.com/ralf1307/pmaports/-/tree/feature%2Flomiri) for patches related to Lomiri
