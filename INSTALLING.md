# Installation
When downloading all rpms, you can run
```
sudo dnf install -y ./*/*.rpm
```

To remove all:
```
for i in ./*/*.rpm; do sudo dnf -y remove $(basename "$i" | sed "s/.rpm$//g"); done
```
