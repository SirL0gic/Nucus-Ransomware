# Nucus-Ransomware

Disclaimer: This post is for research and educational purposes only. I do not take any responsibility, in regards to the actions taken by readers of this article. Never attempt to hack a device for which you do not have the required permissions to do so.

The word Nucus comes from the Latin term _Enucleatus_ which means simple. Nonetheless, this ransomware shows how easy it can be it wreak havoc havoc on a system or a network.

The ransomware that was created is made using the Python programming language. It is divided into three units:

1.  The Command and Control server called `candc.py`
2.  The Malware itself that is used for encryption called `malware.py`
3.  The Decryption file called `decrypter.py`


### Command and Control Server

The CandC server consists of two parts. The first part is to initiate the server, which
then listens to incoming connections. Once the victim runs `malware.py` on their computer
the files get encrypted and the key is set to this server. After that a ”chat” socket is opened
to discuss the ransom between the victim and the attacker.

### Malware

This is the actual ransomware, first it generates the key and sends it to the CnadC server.
After that it locates file extensions on system such as `.pdf .txt .docx` etc and encrypts them
using the same key. After encrypting the files, the original files are then deleted and replaced
by the encrypted ones.

The key is generated using Fernet python library, it is AES128 in CBC mode with a
SHA256 HMAC message authentication code. A Fernet key is the base64url encoding of the
following fields: Signing-key ‖ Encryption-key. The Signing-key and encryption key is 128
bits. Also the fernet token is the base64url encoding of the concatenation of the following
fields: Version ‖ Timestamp ‖ IV ‖ Ciphertext ‖ HMAC .



### Decrypter

When the victim runs this file, it first allows the victim to connect with the attacker
and ”chat”. Once the attacker is satisfied with the ransom, he/she sends the decrpytion
key over the socket connection. The victim then, is able to input the key via CLI into the
Decrpyter. Once that is done, the decrypter located all encrypted files, then decrpyts them
and then deleted the encrypted files. Now the vicitm has all his/her files back as they were
before the attack

### Demo
![alt text](https://i.imgur.com/CsftzWX.jpg)
![alt text](https://i.imgur.com/flmejfh.jpg)
![alt text](https://i.imgur.com/ygVezlZ.jpg)
![alt text](https://i.imgur.com/ESzXIE3.jpg)


### Anti Virus Testing

VirusTotal inspects items with over 70 antivirus scanners and URL/domain blocklisting services, in addition to a myriad of tools to extract signals from the studied content. Any user can select a file from their computer using their browser and send it to VirusTotal

Malware signatures are updated frequently by VirusTotal as they are distributed by antivirus companies, this ensures that our service uses the latest signature sets.

Website scanning is done in some cases by querying vendor databases that have been shared with VirusTotal and stored on our premises, and in other cases by API queries to an antivirus company's solution. As such, as soon as a given contributor blocklists a URL it is immediately reflected in user-facing verdicts.

VirusTotal not only tells you whether a given antivirus solution detected a submitted file as malicious, but also displays each engine's detection label (e.g., I-Worm.Allaple.gen). The same is true for URL scanners, most of which will discriminate between malware sites, phishing sites, suspicious sites, etc. Some engines will provide additional information, stating explicitly whether a given URL belongs to a particular botnet, which brand is targeted by a given phishing site, and so on.

**According to a scan using Virus Total. There were `0` detections on `[malware.py](http://malware.py)` from the 58 engines that were used, this includes engines like Kaspersky, Norton, McAfee, Symantec and F-Secure.**


![alt text](https://i.imgur.com/K0HmDn1.png)
