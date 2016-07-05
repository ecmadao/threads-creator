from setuptools import setup, find_packages

setup(
    name='threads_creator',
    version='1.5',
    keywords=('spider', 'thread'),
    description='A tool to help you build multiply spider',
    author='ecmadao',
    author_email='wlec@outlook.com',
    url='https://github.com/ecmadao/threads-creator',
    packages=find_packages(),
    py_modules=['run'],
    include_package_data=True,
    platforms='any',
    install_requires=[],
    license='MIT',
    zip_safe=False,
    classifiers=[
         'Environment :: Console',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3.5',
         'Programming Language :: Python :: Implementation :: CPython'
    ]
)
