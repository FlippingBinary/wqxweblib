import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="wqxlib",
  version="0.1.0",
  author="Jon Musselwhite",
  author_email="JMusselwhite@wvstateu.edu",
  description="A package for interacting with the EPA's WQX service",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/FlippingBinary/wqxlib",
  packages=["enum","hashlib","base64","datetime","hmac","re","requests"],
  classifiers=[
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Hydrology",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
  python_requires='>=3.6',
)