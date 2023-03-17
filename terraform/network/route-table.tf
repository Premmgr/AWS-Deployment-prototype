resource "aws_route_table" "stage-route-table" {
  vpc_id = aws_vpc.stage-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.stage-gw.id
  }

  tags = {
    Name = "stage-route-table"
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.stage-subnet.id
  route_table_id = aws_route_table.stage-route-table.id
}