---
title: "Using different ssh keys for multiple github accounts"
date: 2022-02-20T11:15:00+07:00
categories:
  - blog
tags:
  - ssh
  - github
---
Description

### Add member to your repository
### Genergate ssh keys
```sh
$ ssh-keygen -t rsa -C "account1@email.com"
$ ssh-keygen -t ed25519 -C "account2@organization_email.com"
```

### Edit ssh config 
`vi ~/.ssh/config`

```sh
Host github.com-account1
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa

Host github.com-account2
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_account2
```
### Add your ssh key to the repository
### Clone your repository