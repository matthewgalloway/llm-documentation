FROM hashicorp/terraform:1.5

RUN apk add --update \
    python3 \
    py3-pip \
&& pip3 install --upgrade pip \
&& pip3 install awscli \
&& apk --purge -v del py-pip \
&& rm -rf /var/cache/apk/*  