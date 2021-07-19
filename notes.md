# create a go-helloworld Deployment in namespace `test`
kubectl create deploy go-helloworld --image=quantranxd/go-helloworld:v1.0.0 -n test

# forward a local port to a port on the Pod (pod belongs to deploy/go-helloworld; can be deploy/rs/po)
kc port-forward deploy/go-helloworld 6969:6112

`kubectl port-forward <pod-name> <locahost-port>:<pod-port>`

# pull off a new pod to test internal connectivity
`kc run test-$RANDOM -n default --rm -it --image=alpine -- sh
wget -qO- clusterIp:port`
