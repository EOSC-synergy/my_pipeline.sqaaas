(cat <<EOF >> ./kustomization.yaml
resources:
- ./deployment_1.yaml
- ./deployment_2.yaml
EOF
kubectl apply -k .
if ! kubectl rollout status -k . --timeout=0s; then
    kubectl rollout undo -k . --timeout=0s
    kubectl rollout status -k . --timeout=0s
fi
)