data "aws_vpc" "selected" {
  filter {
    name   = "tag:Name"
    values = ["stage"]
  }
}

resource "aws_security_group" "sec-grp" {
  name        = "sec-grp"
  description = "security group that allows various protocol"
  vpc_id      = data.aws_vpc.selected.id

# allow ssh protocol
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
# allow sftpd protocol
  ingress {
    from_port   = 21
    to_port     = 21
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

# allow http protocol
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
# allow application port
  ingress {
    from_port   = 800
    to_port     = 800
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

# add ping protocol (ICMP)

  ingress {
    from_port   = -1
    to_port     = -1
    protocol    = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
