## default.nix
#with (import <nixpkgs> {});
#mkShell {
#  buildInputs = [
#    python311
#    python311Packages.pyside6
#    python311Packages.numpy
#    python311Packages.opencv4
#    python311Packages.pyzmq
#    python311Packages.sympy
#  ];
#}

# let
#   pkgs = import <nixpkgs> {};
# in pkgs.mkShell {
#   packages = [
#     (pkgs.python3.withPackages (python-pkgs: [
#       python-pkgs.pyside6
#       python-pkgs.pyside2
#       python-pkgs.numpy
#       python-pkgs.sympy
#       python-pkgs.opencv4
#       python-pkgs.pyzmq
#       python-pkgs.pyqtgraph
#       python-pkgs.pyqt6
#       pkgs.libsForQt5.qt5.wrapQtAppsHook
#     ])
#     )
#   ];
# }

# save this as shell.nix
{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.pyside6
      #python-pkgs.pyside2
      python-pkgs.numpy
      #python-pkgs.sympy
      python-pkgs.opencv4
      #python-pkgs.pyzmq
      python-pkgs.pyqtgraph
      #python-pkgs.pyqt6
      #pkgs.libsForQt5.qt5.wrapQtAppsHook
      pkgs.pyright
    ])
    )
  ];
}

# also need to install nixgl, https://github.com/guibou/nixGL
# and nixGL python3 main.py
