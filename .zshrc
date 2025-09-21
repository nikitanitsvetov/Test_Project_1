#vpn up
skup() {
  vpnutil start skai &
  wait $!
  local timeout=30  # Maximum wait time in seconds
  local elapsed=0
  while ! vpnutil status skai | grep -q "Connected"; do
    if (( elapsed >= timeout )); then
      echo "Error: VPN did not connect within $timeout seconds."
return 1 fi
    echo "Waiting for VPN to be fully connected..."
    sleep 1
    (( elapsed++ ))
done
  ~/skai-vpn-routes.sh
}
#vpn down
skdown() {
  vpnutil stop skai &
  wait $!
  local timeout=30  # Maximum wait time in seconds
  local elapsed=0
while ! vpnutil status skai | grep -q "Disconnected"; do
if (( elapsed >= timeout )); then
      echo "Error: VPN did not disconnect within $timeout seconds."
      return 1
    fi
    echo "Waiting for VPN to be fully disconnected..."
    sleep 1
    (( elapsed++ ))
done
  ~/skai-vpn-routes.sh
}