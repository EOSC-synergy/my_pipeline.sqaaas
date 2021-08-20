#!/bin/bash
###
# Shell script to update Domain Name o3as.test.fedcloud.de
# with the right IP.
###

LOGFILE="nsupdate-fedcloud.log"
SITE="api.o3as.fedcloud.eu"
SECRET="SSEECCRREETT"
echo $(date +"%F %T %Z") >> ${LOGFILE}
curl https://$SITE:$SECRET@nsupdate.fedcloud.eu/nic/update >> ${LOGFILE}
echo "" >> ${LOGFILE}

