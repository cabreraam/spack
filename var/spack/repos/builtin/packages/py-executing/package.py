# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyExecuting(PythonPackage):
    """Get the currently executing AST node of a frame, and other information."""

    homepage = "https://github.com/alexmojaki/executing"
    pypi = "executing/executing-0.8.2.tar.gz"

    version("1.1.0", sha256="2c2c07d1ec4b2d8f9676b25170f1d8445c0ee2eb78901afb075a4b8d83608c6a")
    version("0.8.2", sha256="c23bf42e9a7b9b212f185b1b2c3c91feb895963378887bb10e64a2e612ec0023")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm+toml", type="build")
