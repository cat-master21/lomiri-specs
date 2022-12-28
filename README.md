# lomiri-specs
Lomiri/Unity8 RPM spec files for Fedora
**Currently this fails with:**
```
(process:15757): GLib-GIO-ERROR **: 20:57:15.067: Settings schema 'com.lomiri.keyboard.maliit' is not installed
Trace/breakpoint trap
```

## Created spec files list:
### Needed for Lomiri to build:
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

### Extra applications/functionality for Lomiri:
* [] lomiri-terminal
* [X] lomiri-system-compositor
* [] ubuntu-touch-session
* [X] lomiri-desktop-session
* [X] suru-icon-theme
* [] ubuntu-sdk
* [] Fix some sections of lomiri-system-settings
	* [] lomiri-keyboard
	* [] lomiri-system-settings-*
	* [] ayatana-indicator-datetime

## Thanks To
* [lomiri-on-fedora](https://gitlab.com/erlend.io/lomiri-on-fedora) for examples on how to build some RPMs