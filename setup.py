from setuptools import setup

setup(
    name='Flask-Jenkins',
    version='0.1.0',
    packages=['flask_jenkins'],
    url='https://github.com/Earrow/flask-jenkins',
    author='Earrow',
    author_email='earrow.liu@gmail.com',
    description='Adds Jenkins support to Flask',
    keywords=['jenkins'],
    install_requires=['python-jenkins>=0.4.16'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
