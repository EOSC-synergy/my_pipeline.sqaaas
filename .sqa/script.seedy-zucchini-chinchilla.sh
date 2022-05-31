(mkdir /im
cat <<EOF >> /im/auth.dat
# InfrastructureManager auth
type = InfrastructureManager; username = %s; password = %q
# OpenStack site using standard user, password, tenant format
id = incd; type = OpenStack; host = https://stratus.ncg.ingrid.pt:5000; username = %s; password = %q; tenant = None; domain = default; auth_version = 3.x_password
EOF
printf "$(cat /im/auth.dat)" "${IM_USER}" "${IM_PASS}" "${OPENSTACK_USER}" "${OPENSTACK_PASS}" > /im/auth.dat
echo "Generated auth.dat file:"
ls -l /im/auth.dat
printf "$(cat )" "https://stratus.ncg.ingrid.pt" "" > /im/test-ost.tosca
echo "Printing tosca file"
cat /im/test-ost.tosca
echo
im_client.py -r "https://appsgrycap.i3m.upv.es:31443/im/" -a "/im/auth.dat" create_wait_outputs /im/test-ost.tosca > ./im_tosca.json
RETURN_CODE=$?
echo "im_client.py create_wait_outputs return code: ${RETURN_CODE}"
echo "Infrastructure Manager output:"
cat ./im_tosca.json
awk "/\{/,/\}/ { print $1 }" ./im_tosca.json > ./im_tosca_aux.json
echo "Infrastructure Manager output (only json part):"
cat ./im_tosca_aux.json
echo
INFID=$(jq -r '[ .infid ] | .[]' ./im_tosca_aux.json)
echo "INFID=${INFID}"
if [ ${RETURN_CODE} -eq 0 ] && ! [[ -z "${INFID}" && "x${INFID}x" == "xnullx" ]]; then
  echo "Deployment finished with success. Logs:"
  im_client.py -r "https://appsgrycap.i3m.upv.es:31443/im/" -a "/im/auth.dat" getcontmsg ${INFID}
  echo
  im_client.py -r "https://appsgrycap.i3m.upv.es:31443/im/" -a "/im/auth.dat" destroy ${INFID}
  echo "im_client.py destroy return code: $?"
elif ! [[ -z "${INFID}" && "x${INFID}x" == "xnullx" ]]; then
  echo "Deployment failed. Logs:"
  im_client.py -r "https://appsgrycap.i3m.upv.es:31443/im/" -a "/im/auth.dat" getcontmsg ${INFID}
  echo
  im_client.py -r "https://appsgrycap.i3m.upv.es:31443/im/" -a "/im/auth.dat" destroy ${INFID}
  echo "im_client.py destroy return code: $?"
  exit ${RETURN_CODE}
else
  exit ${RETURN_CODE}
fi
)