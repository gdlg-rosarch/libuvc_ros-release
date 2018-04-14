Name:           ros-lunar-libuvc-camera
Version:        0.0.10
Release:        1%{?dist}
Summary:        ROS libuvc_camera package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/libuvc_camera
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-camera-info-manager
Requires:       ros-lunar-dynamic-reconfigure
Requires:       ros-lunar-image-transport
Requires:       ros-lunar-libuvc
Requires:       ros-lunar-nodelet
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-camera-info-manager
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-dynamic-reconfigure
BuildRequires:  ros-lunar-image-transport
BuildRequires:  ros-lunar-libuvc
BuildRequires:  ros-lunar-nodelet
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-sensor-msgs

%description
USB Video Class camera driver

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Sat Apr 14 2018 Ken Tossell <ken@tossell.net> - 0.0.10-1
- Autogenerated by Bloom

* Fri Apr 13 2018 Ken Tossell <ken@tossell.net> - 0.0.10-0
- Autogenerated by Bloom

* Tue Oct 10 2017 Ken Tossell <ken@tossell.net> - 0.0.9-1
- Autogenerated by Bloom

* Thu Jun 15 2017 Ken Tossell <ken@tossell.net> - 0.0.9-0
- Autogenerated by Bloom

* Thu Jun 15 2017 Ken Tossell <ken@tossell.net> - 0.0.8-0
- Autogenerated by Bloom

