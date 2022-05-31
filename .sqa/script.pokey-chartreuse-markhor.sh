(printf "$(cat /im/auth/auth.dat)" "${IM_USER}" "${IM_PASS}" incd "https://stratus.ncg.ingrid.pt:5000" "${OPENSTACK_USER}" "${OPENSTACK_PASS}" None default 3.x_password > /im/auth/auth.dat
echo "Generated auth.dat file:"
ls -l /im/auth/auth.dat
printf "$(cat )" "https://stratus.ncg.ingrid.pt" "" > /im/test-ost.tosca
echo "Printing tosca file"
cat /im/test-ost.tosca
echo
im_client.py -r "https://appsgrycap.i3m.upv.es:31443/im/" -a "/im/auth/auth.dat" create_wait_outputs /im/test-ost.tosca > ./im_tosca.json
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
  im_client.py -r "https://appsgrycap.i3m.upv.es:31443/im/" -a "/im/auth/auth.dat" getcontmsg ${INFID}
  echo
  im_client.py -r "https://appsgrycap.i3m.upv.es:31443/im/" -a "/im/auth/auth.dat" destroy ${INFID}
  echo "im_client.py destroy return code: $?"
elif ! [[ -z "${INFID}" && "x${INFID}x" == "xnullx" ]]; then
  echo "Deployment failed. Logs:"
  im_client.py -r "https://appsgrycap.i3m.upv.es:31443/im/" -a "/im/auth/auth.dat" getcontmsg ${INFID}
  echo
  im_client.py -r "https://appsgrycap.i3m.upv.es:31443/im/" -a "/im/auth/auth.dat" destroy ${INFID}
  echo "im_client.py destroy return code: $?"
  exit ${RETURN_CODE}
else
  exit ${RETURN_CODE}
fi
)