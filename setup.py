from distutils.core import setup

setup(
  name = 'NBSapi', 
  packages = ['NBSapi'], 
  version = '0.6', 
  license=' GPL-3.0', 
  description = 'a python library that helps you to control the sapi5 TTS', 
  author = 'nacer baaziz', 
  author_email = 'nacerbaaziz@ng-space.com', 
  url = 'https://github.com/baaziznasser/nbsapi', 
  download_url = 'https://github.com/baaziznasser/nbsapi/archive/refs/tags/0.5.tar.gz', 
  keywords = ['nbsapi', 'NBSapi', 'Sapi', 'tts', 'python text to speech', 'audio', 'screen reader', 'voices', 'sapi5', 'spvoice', 'text to speech', 'audio book'], 
  install_requires=[            
          'comtypes',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
],
)