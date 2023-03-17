resource "aws_subnet" "stage-subnet" {
  vpc_id     = aws_vpc.stage-vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "stage"
  }
}