FROM alpine

ADD entry /usr/local/bin/entry

ENTRYPOINT ["/usr/local/bin/entry"]
