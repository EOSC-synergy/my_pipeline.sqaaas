(
mkdir /im
cat <<EOF >> /im/auth.dat
# InfrastructureManager auth
type = InfrastructureManager; username = %s; password = %s
# OpenStack site using standard user, password, tenant format
id = ifca; type = OpenStack; host = https://api.cloud.ifca.es:5000; username = %s; password = %s; tenant = VO:eosc-synergy.eu; tenant_domain_id = 0432c17d955e4c8d8ab7db0384536d4e; domain = EOSC-Synergy; auth_version = 3.x_password
EOF
if [ -z "$IM_USER" ] || [ -z "$IM_PASS" ] || [ -z "$OPENSTACK_USER" ] || [ -z "$OPENSTACK_PASS" ]; then
  echo 'One or more credential variables are undefined (required: IM_USER, IM_PASS, OPENSTACK_USER, OPENSTACK_PASS)'
  exit 1
fi
printf "$(cat /im/auth.dat)" "${IM_USER}" "${IM_PASS}" "${OPENSTACK_USER}" "${OPENSTACK_PASS}" > /im/auth.dat
echo "Generated auth.dat file:"
ls -l /im/auth.dat
echo "*****************"
cat /im/auth.dat
echo "*****************"

ec3 launch jepl_im_cluster kubernetes ubuntu-ost -a "/im/auth.dat" -u https://appsgrycap.i3m.upv.es:31443/im/ -y
ec3 show jepl_im_cluster -r
ec3 destroy jepl_im_cluster --force -y
)
