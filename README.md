# hermes-keystoneauth

Fork of the OpenStack Swift Keystone Auth middleware that adds a config option
to specify read-only roles.

The original keystoneauth middleware can be found here:
https://github.com/openstack/swift/blob/master/swift/common/middleware/keystoneauth.py

If specified in the proxy-server config, users who would otherwise fail
authorization may be granted read-only access to accounts, containers, and
objects if they have a role that is listed in the `readonly_roles` config
parameter.

This makes swift users with this role more akin to regular unix users (on a
system with a typical umask) where they can read everything unless otherwise
specified.

Read-only users can be explicitly granted write access to certain containers
using the regular swift ACL mechanism.

Relevant section from config file:
```
# hermes_keystoneauth extension:
# We add support for read-only users who have full access to an account
# but can only perform read (GET, HEAD) queries. These users can also
# have explicit write ACLs set to extend limited write access.
readonly_roles = swiftro
#
```

## Installing

```
git clone git@github.com:caida/hermes-keystoneauth
python setup.py install
```

## Configuration

To use this middleware, replace the `keystoneauth` middleware in your proxy
server pipeline with `hermes_keystoneauth`, and change the keystoneauth config
section to refer to `hermes_keystoneauth` instead of `keystoneauth` like so:

```
[filter:hermes_keystoneauth]
use = egg:hermes_keystoneauth#hermes_keystoneauth
...
```

Additionally, this fork introduces the `readonly_roles` config option described
above. This is set in the same manner as the `operator_roles` option. For
example:
```
readonly_roles = swiftro
```

## Changes introduced

The code changes introduced in this fork are all found in a single commit:
https://github.com/CAIDA/hermes-keystoneauth/commit/431fb9d6d447d71fd6bce181013753f7599bb5ce
but if you want to be sure, download the original and run a diff ;)
