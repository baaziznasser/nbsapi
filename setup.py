from distutils.core import setup
setup(
  name = 'NBSapi', 
  packages = ['NBSapi'], 
  version = '1.0', 
  license=' GPL-3.0', 
  description = 'a python class that helps you to control the sapi5 TTS', 
  author = 'nacer baaziz', 
  author_email = 'nacerbaaziz@ng-space.com', 
  url = 'https://github.com/baaziznasser/nbsapi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz', 
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            
          'pywin32',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GPL-3.0 License', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
],
)