import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lucidsonicdreams", 
    version="0.4",
    author="Alain Mikael Alafriz",
    author_email="mikaelalafriz@gmail.com",
    description="Syncs GAN-generated visuals to music",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mikaelalafriz/lucid-sonic-dreams",
    download_url="https://github.com/mikaelalafriz/lucid-sonic-dreams/archive/v_04.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['tensorflow==1.15',
                      'librosa<=0.8.1',
                      'numpy<=1.20.2',
                      'moviepy==1.0.3',
                      'Pillow<=8.2.0',
                      'tqdm<=4.6.0',
                      'scipy<=1.6.2',
                      'scikit-image<=0.18.2',
                      'pygit2<=1.6.0',
                      'gdown<=3.10.2', 
                      'mega.py<=1.0.8',
                      'requests<=2.26.0',
                      'pandas<=1.2.4',
                      'SoundFile<=0.10.3.post1']
)
