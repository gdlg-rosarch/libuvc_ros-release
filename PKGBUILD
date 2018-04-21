# Script generated with Bloom
pkgdesc="ROS - USB Video Class camera driver"
url='http://ros.org/wiki/libuvc_camera'

pkgname='ros-lunar-libuvc-camera'
pkgver='0.0.10_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-camera-info-manager'
'ros-lunar-catkin'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-transport'
'ros-lunar-libuvc'
'ros-lunar-nodelet'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
)

depends=('ros-lunar-camera-info-manager'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-transport'
'ros-lunar-libuvc'
'ros-lunar-nodelet'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
)

conflicts=()
replaces=()

_dir=libuvc_camera
source=()
md5sums=()

prepare() {
    cp -R $startdir/libuvc_camera $srcdir/libuvc_camera
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

