mfa-aws
=======

Helper script for using MFA with the aws cli. Requires python3.

Usage
-----

.. code:: bash

   usage: mfa-aws [options]

   updates aws credentials file with temporary sts credentials obtained with mfa

   optional arguments:
     -h, --help            show this help message and exit
     -d, --debug           Enable debug
     -c CONFIG_FILE, --config-file CONFIG_FILE
                           config file to load mfa details [~/.aws/mfa-config]
     -p PROFILE, --profile PROFILE
                           profile to be loaded from the config file [default]

Example
-------

Before
~~~~~~

**[~/.aws/credentials]**
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: bash

   [default]
   aws_access_key_id = ASIADSJFKDSF3242
   aws_secret_access_key = FDSFSDKJFd/fdsfSDFSFfDSF4837fdDSFHDKSFsd0D

   [other-account-default]
   aws_access_key_id = ASIADSGFDDFG3897
   aws_secret_access_key = DFGKSJGSDKJGSDKJ4636//43643KJ353KJH/KFDFSDFS/DLKDKSFsd0D

**[~/.aws/mfa-config]**
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: bash

   [profile default]
   mfa_serial = arn:aws:iam::111111111111:mfa/username
   dest_profile = default-mfa

   [profile other-account]
   mfa_serial = arn:aws:iam::999999999999:mfa/username
   dest_profile = other-account-mfa
   source_profile = other-account-default
   mfa_secret = 4HIANG4VIUY5SUVL22L2QDRX7Q7EQAUUKZC5QTWNHKSEQDEW2TOFZUMIQROTFPU3

Run
~~~

.. code:: bash

   MBP-USERNAME:~ username$ mfa-aws
   token code for arn:aws:iam::111111111111:mfa/username: 111111
   Updated credentials for default-mfa
   MBP-USERNAME:~ username$
   MBP-USERNAME:~ username$ mfa-aws -p other-account
   Updated credentials for other-account-mfa
   MBP-USERNAME:~ username$

After
~~~~~

.. _awscredentials-1:

**[~/.aws/credentials]**
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: bash

   [default]
   aws_access_key_id = ASIADSJFKDSF3242
   aws_secret_access_key = FDSFSDKJFd/fdsfSDFSFfDSF4837fdDSFHDKSFsd0D

   [other-account-default]
   aws_access_key_id = ASIADSGFDDFG3897
   aws_secret_access_key = DFGKSJGSDKJGSDKJ4636//43643KJ353KJH/KFDFSDFS/DLKDKSFsd0D

   [default-mfa]
   aws_access_key_id = ASIADSJFKDSF3242
   aws_secret_access_key = FDSFSDKJFd/fdsfSDFSFfDSF4837fdDSFHDKSFsd0D
   aws_session_token = RIKJSFSAFJAS128753718965/352523//35jfhdssdDSJFKRIKJSFSAFJAS128753718965/352523//35jfhdssdDSJFKRIKJSFSAFJAS128753718965/352523//35jfhdssdDSJFK

   [other-account-mfa]
   aws_access_key_id = ASIADSGFDDFG3897
   aws_secret_access_key = DFGKSJGSDKJGSDKJ4636//43643KJ353KJH/KFDFSDFS/DLKDKSFsd0D
   aws_session_token = DFKJSF8732ASFAJKFHFHK324423/rekjAF/33kjfDFJKKJFDDFKJSF8732ASFAJKFHFHK324423/rekjAF/33kjfDFJKKJFDDFKJSF8732ASFAJKFHFHK324423/rekjAF/33kjfDFJKKJFD
