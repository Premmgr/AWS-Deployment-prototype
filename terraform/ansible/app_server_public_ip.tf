data "aws_instance" "app_server" {
  filter {
    name   = "tag:Name"
    values = ["app-server"]
  }
  filter {
    name   = "instance-state-name"
    values = ["running"]
  }
}

resource "null_resource" "save_appserver_ip" {
  depends_on = [data.aws_instance.app_server]

  provisioner "local-exec" {
    command = "echo '${data.aws_instance.app_server.public_ip}' > app_server_ip"
  }
}

resource "local_file" "hosts" {
  depends_on = [null_resource.save_appserver_ip]

  content  = "${data.aws_instance.app_server.public_ip}"
  filename = "hosts"
}