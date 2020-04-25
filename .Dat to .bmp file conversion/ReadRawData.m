function x = ReadRawData(filename)

% Open fle
id = fopen(filename, 'r');

%precision = 'uint8';
channels = str2num(fgetl(id));
height = str2num(fgetl(id));
width = str2num(fgetl(id));
prec = str2num(fgetl(id));
if prec == 0
    precision = 'uint8';
elseif prec == 2
    precision = 'uint16';
% TODO support other types    
end
%precision = 'uint16';
% Read in the data.
x1 = fread(id, width * height * channels, precision, 0, 'l');
x2 = reshape(x1,[channels, width, height]);
x = permute(x2, [3 2 1]);

if prec == 0
    x = uint8(x);
end

% Close file
fclose(id);
