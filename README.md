```
git clone https://github.com/kamibook/rpmbuild.git

tar -zxvf steamp-0.1.4-x86_64-unknown-linux-musl.tar.gz

cp steamp rpmbuild/SOURCES/

rpmbuild -bb ~/rpmbuild/SPECS/steamp.spec
```
