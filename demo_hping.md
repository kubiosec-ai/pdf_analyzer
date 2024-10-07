# HPING Tutorial

**by Philippe Bogaerts, alias xxradar**  
**Version 1.5 24-08-2003**  
Website: [radarhack.com](http://www.radarhack.com)  
Contact: [xxradar@radarhack.com](mailto:xxradar@radarhack.com)  

## What is HPING?

Hping is a command-line oriented TCP/IP packet crafting tool. It allows users to create IP packets with TCP, UDP, or ICMP payloads. Every header field can be adjusted and controlled using the command line. Users must understand IP and TCP/UDP protocols to effectively utilize this tool. For more information and to download binaries, visit [hping.org](http://www.hping.org). A full working version can be found on a bootable CD with other tools at [knoppix-std.org](http://www.knoppix-std.org).

**Important:** Use all examples within a test environment to avoid unintended negative impacts on networks, such as slowing down or crashing firewalls or end systems.

## Key Features and Techniques

### 1. HPING as a Port Scanner

Hping's default behavior is crafting TCP packets. By specifying TCP flags, a destination port, and a target IP address, one can construct TCP packets. Below are some of the TCP flags that Hping can set:

- `-F`, `--fin`: Set FIN flag
- `-S`, `--syn`: Set SYN flag
- `-R`, `--rst`: Set RST flag
- `-P`, `--push`: Set PUSH flag
- `-A`, `--ack`: Set ACK flag
- `-U`, `--urg`: Set URG flag
- `-X`, `--xmas`: Set X unused flag (0x40)
- `-Y`, `--ymas`: Set Y unused flag (0x80)

#### Example Usage

To send SYN packets to port 80 on IP 192.168.10.1:

```bash
[root@localhost root]# hping -I eth0 -S 192.168.10.1 -p 80
```

**SYN Scan (Stealth Scan):** This technique identifies open ports based on SA return packets (SYN-ACK) for open ports and RA (RST-ACK) packets for closed ports.

#### Incremental Port Scanning

You can increment the destination port using `++` or by pressing `ctrl+z` during the scan:

```bash
[root@localhost root]# hping -I eth0 -S 192.168.10.1 -p ++79 | grep SA
```

This tool replicates most of the known NMAP scanning techniques with finer control over packets.

### 2. Idle Scanning

Idle scanning is a method to conduct anonymous port scans. It relies on a silent host, which must have a predictable IP ID increment. This is an advanced technique that allows indirect mapping of the target's open ports.

### 3. Firewall Mapping

Hping can function in traceroute or Firewalk style using ICMP, UDP, or TCP packets to scan and probe firewalls for potential vulnerabilities or mapping purposes.

### 4. HPING for Denial of Service (DoS) Testing

Although not intended to cause real damage, Hping can be used to simulate DoS conditions to test IDS/firewall setups.

#### 4.1 SYN Attack

This involves sending a flood of SYN packets to test a target's ability to handle TCP connection requests.

```bash
[root@localhost root]# hping -I eth0 -a 192.168.10.99 -S 192.168.10.33 -p 80 -i u1000
```

#### 4.2 LAND Attack

Crafting a packet to cause a machine to connect a socket to itself, historically effective against older Windows NT systems.

### 5. Crafting Packets with Signatures

Hping allows the construction of packets with specific signatures, making it possible to simulate certain network behaviors or vulnerabilities such as buffer overflow attacks.

### 6. Transferring Files via ICMP, UDP, or TCP

#### 6.1 File Transfer via ICMP

By using the `--listen` feature, Hping can listen for specific signatures within incoming packets, allowing pseudo-file transfers over unusual protocols like ICMP:

```bash
[root@localhost root]# hping 192.168.10.66 --listen signature --safe --icmp
```

#### 6.2 File Transfer via TCP

Even in the presence of state-aware firewalls, using crafted packets without the need for a full TCP session:

```bash
[root@localhost root]# hping 192.168.10.66 --listen signature --safe -p 22
```

### 7. Using HPING as a Trojan

Hping can be manipulated to execute commands on a remote machine if it can be started on that host, effectively acting as a control utility.

### Conclusion

HPING is a valuable tool for understanding TCP/IP protocols, auditing firewalls/IDS systems, and experimenting with packet-crafting. However, usage must be responsible to prevent unauthorized damage. It is recommended for educational, security auditing, and personal enjoyment purposes only.

**Feedback and remarks are welcome at:** [xxradar@radarhack.com](mailto:xxradar@radarhack.com)

The Markdown document provides a clean and organized presentation of the original tutorial while preserving all technical details. It highlights important points, provides contextual explanations, and organizes content into sections with examples and commands in code blocks for clarity.
