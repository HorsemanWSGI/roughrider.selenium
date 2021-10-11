import os
from setuptools import setup, find_packages


version = "0.1"

install_requires = [
    'pytest',
    'selenium',
    'bjoern',
]

test_requires = [
]


setup(
    name='nva.selenium',
    version=version,
    author='Novareto GmbH',
    author_email='trollfot@gmail.com',
    url='https://github.com/novareto/nva.selenium',
    download_url='http://pypi.python.org/pypi/nva.selenium',
    description='Testing WSGI applications with Selenium',
    long_description=(open("README.rst").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.rst")).read()),
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['nva',],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
    },
    entry_points={
        "pytest11": [
            "nva.selenium = nva.selenium:wsgi_selenium"
        ],
    }
)
