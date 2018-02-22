from conans import ConanFile, CMake, tools
import os
from conans.tools import os_info, SystemPackageTool

class SfmlConan(ConanFile):
    name = "sfml"
    version = "2.4.2"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "SFML is a simple, fast, cross-platform and object-oriented multimedia API. It provides access to windowing, graphics, audio and network. It is written in C++, and has bindings for various languages such as C, .Net, Ruby, Python."
    settings = "os", "compiler", "build_type", "arch"
    options = None
    default_options = None
    generators = "cmake"

    def system_requirements(self):
        pack_name = None
        if os_info.linux_distro == "ubuntu":
            pack_name = ["libopenal-dev", "libvorbis-dev", "libflac-dev"]
    
        if pack_name:
            installer = SystemPackageTool()
            installer.install(pack_name)  # Install the package, will update the package database if pack_name isn't already installed
        
    def source(self):
        self.run("git clone https://github.com/SFML/SFML.git")
        self.run("cd SFML && git checkout tags/2.4.2")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="SFML")
        cmake.definitions["BUILD_SHARED_LIBS"] = "ON"
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = "install"
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="install/include")
        self.copy("*.lib", dst="lib", src="install/", keep_path=False)
        self.copy("*.dll", dst="bin", src="install/", keep_path=False)
        self.copy("*.so", dst="lib", src="install/", keep_path=False)
        self.copy("*.dylib", dst="lib", src="install/", keep_path=False)
        self.copy("*.a", dst="lib", src="install/", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["sfml-audio", "sfml-graphics", "sfml-network", "sfml-system", "sfml-window"]
        
        #self.cpp_info.libs.append("sfml-main")
        
        if self.settings.build_type == "Debug":
            self.cpp_info.libs = [l + "-d" for l in self.cpp_info.libs]
