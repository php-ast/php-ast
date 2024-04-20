PHP_RELEASE := 8.3.1
PHP_MIRROR := http://php.net

PHP_MAJOR := $(firstword $(subst ., ,$(PHP_RELEASE)))
PHP_SRC := php-$(PHP_RELEASE).tar.bz2
PHP_DIR := php-$(PHP_RELEASE)
PHP := bin/php
PHP_INC := include/php
PHP_LIB := lib/libphp$(PHP_MAJOR).a

# these flags are not exported and will not affect PHP build
CFLAGS := -g -Wall -Wextra -Werror -Iinclude/php -I$(PHP_INC)/Zend -I$(PHP_INC)/TSRM -I$(PHP_INC)/main
LDFLAGS := -lm

all: $(PHP_LIB) payload-phar.c

.PHONY: all clean distclean

clean:
	$(RM) -r $(PHP_DIR) bin include lib payload.phar payload-phar.c

distclean: clean
	$(RM) $(PHP_SRC)

$(PHP_SRC): 
	wget --no-verbose $(PHP_MIRROR)/distributions/$(PHP_SRC)

$(PHP): $(PHP_SRC)
	tar --extract --file $(PHP_SRC)
	cd $(PHP_DIR) && for PATCHFILE in ../patches/*.patch; do echo "applying $${PATCHFILE}" && patch -p1 <"$${PATCHFILE}"; done
	cd $(PHP_DIR) && ./buildconf --force && CFLAGS='-O2 -fPIC' ./configure  --prefix='$(realpath .)'  --enable-embed=static --disable-phpdbg --disable-cgi --disable-all --enable-ast --enable-ctype --enable-filter --enable-json --enable-tokenizer --enable-phar --without-pear --enable-debug
	$(MAKE) -C $(PHP_DIR) install-cli install-headers install-sapi
	$(CC) $(SHARED) -o $(PHP_SO) $(PHPC_SOURCE) -L./lib -lphp$(PHP_MAJOR) $(CFLAGS) -fPIC

# dummy rule
$(PHP_LIB): $(PHP)

# FIXME: incomplete dependency
payload.phar: $(PHP)
	$(PHP) --define phar.readonly=0 --run '$$phar = new Phar("payload.phar"); $$phar->buildFromDirectory(dirname(__FILE__) . "/payload"); $$phar->setStub($$phar->createDefaultStub("index.php"));'

payload-phar.c: payload.phar
	xxd -i $< >$@


PHP_SO := libphp$(PHP_MAJOR).so
PHPC_SOURCE := php.c payload-phar.c # 根据您的实际文件位置进行调整
SHARED:=-shared
CC:=gcc

phpso: $(PHPC_SOURCE) $(PHP_LIB)
	$(CC) $(SHARED) -o $(PHP_SO) $(PHPC_SOURCE) -L./lib -lphp$(PHP_MAJOR) $(CFLAGS) -fPIC