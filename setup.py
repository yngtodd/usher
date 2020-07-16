from setuptools import setup, find_packages


requirements = ['argh',]
test_requirements = ['pytest>=3', ]
setup_requirements = ['pytest-runner', ]


COMMANDS = [
    'greet = usher.cli:greet',
]


setup(
    author="Todd Young",
    author_email='youngmt1@ornl.gov',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Data loading for token egresses",
    entry_points={'console_scripts': COMMANDS},
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='usher',
    name='usher',
    packages=find_packages(include=['usher', 'usher.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/yngtodd/usher',
    version='0.1.0',
    zip_safe=False,
)
