function commandClient()
%% File header
% title: testClient.m
% author: Dominik Limbach
% date: 08.06.2019
% description:
%     - program creates a tcpip object and sends a message to a python server
%     

%% Set up
port = 8632;
% echotcpip('on', port)
tcp_client = tcpip('localhost', port);

message = 'start';

fopen(tcp_client);
fwrite(tcp_client, message);

A = fread(tcp_client, 2);
res = native2unicode(A)';
disp(res);

fclose(tcp_client);
% echotcpip('off')
end