[Noid4Php](https://github.com/Daniel-KM/Noid4Php) allows for creation of Nice Opaque Identifier (NOID), specifically [ARKs](https://wiki.lyrasis.org/display/ARKs/ARK+Identifiers+FAQ). Noid4Php is a feature equivalent implimentation of the original perl based Noid.

## Exploration

1) Clone the repository 
```
git clone https://github.com/Daniel-KM/Noid4Php
```

2) Before you can use Noid4Php, you need to make sure that dba extension is installed.  To check:
```
php -m
```
To install
```
apt-get install php-7.#-dba
```

3) We can use the executable to execute noid commands.  Note that you need to use `./noid`. 

```
ubuntu:~/Desktop/Noid4Php$ ./noid -help
PHP Warning:  array_shift() expects parameter 1 to be array, string given in /home/nat/Desktop/Noid4Php/noid on line 317
Usage:
               noid [-f Dbdir] [-v] [-h] Command Arguments
               noid -h             (for help with a Command summary).

Usage:
               noid [-f Dbdir] [-v] [-h] Command Arguments
 
 Dbdir defaults to "." if not found from -f or a NOID environment variable.
 For more information try "perldoc noid" or "noid help Command".  Summary:
 ```
 
 4) We need a database to start creating noids.  For example:
 ```
 ubuntu:~/Desktop/Noid4Php$ noid -f /home/nat/Desktop/Noid4Php/test dbcreate s.zd
```
A more complex minter

```
./noid -f /home/nat/Desktop/Noid4Php/test2 dbcreate f5.reedeedk long 13030 digitalscholarship.utsc.utoronto.ca utsc.ca/dsu
```

5) Once we have minter setup.  We can begin creating identifiers.
```
 ./noid -f /home/nat/Desktop/Noid4Php/test2 mint 1
id: 13030/f54x54g11
```

6) Binding
```
ubuntu:~/Desktop/Noid4Php$ ./noid -f /home/nat/Desktop/Noid4Php/test2 bind set 13030/f5wd3q12m locations 'http://digitalscholarship.utsc.utoronto.ca/islandora/object/dsu%3Aroot'
Id:      13030/f5wd3q12m
Element: locations
Bind:    set
```

7) Fetching/checking
```
ubuntu:~/Desktop/Noid4Php$ ./noid -f /home/nat/Desktop/Noid4Php/test2 fetch 13030/f5wd3q12m
id:    13030/f5wd3q12m hold 
Circ:  i|20200807144822|nat/nat|3
locations: http://digitalscholarship.utsc.utoronto.ca/islandora/object/dsu%3Aroot
```

## Questions
* Is default Berkely ./DB sufficient?  Is it scalable?
* 



 
 
 
