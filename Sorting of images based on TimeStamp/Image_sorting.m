function image_sorting(color_img, depth_img, Openpose, selected_color, selected_depth)

%  color_img = 'F:\Daten1\Proband12\GAIT\RG1_color\';
%  depth_img = 'F:\Daten1\Proband12\GAIT\RG1_Depth\';
%  Openpose = 'F:\Daten1\Proband12\GAIT\RG1_color\2dOutput\';
%  selected_color ='F:\Daten1\Proband12\GAIT\RG1_color\selected\';
%  selected_depth ='F:\Daten1\Proband12\GAIT\RG1_Depth\selected';

file = dir(fullfile(depth_img, '*.timestamp'));

file2 = dir(fullfile(color_img, '*.timestamp'));

file3 = dir(fullfile(depth_img, '*.bmp'));

file4 = dir(fullfile(Openpose, '*.png'));

file5 = dir(fullfile(color_img, '*.bmp'));


for k = 1:length(file)
    depthTimestampBase = file(k).name;
    depthTimestamp = fullfile(depth_img,depthTimestampBase);
    
    fileID = fopen(depthTimestamp,'r');
    % format longG
    A(k,:) = textscan(fileID,'%d64') ;
    fclose(fileID);
end


for m = 1:length(file2)

    rgbTimestampBase = file2(m).name;
    rgbTimestamp = fullfile(color_img, rgbTimestampBase);
    
    fileID2 = fopen(rgbTimestamp,'r');
    %format longG
    B(m,:) = textscan(fileID2,'%d64') ;
    fclose(fileID2);
end

%%%%%% Here there are two parts. Use any of them according to conditions
if length(file2) <= length(file)
    %PART 1:- If RGB images are less than depth then use the following code
    %copyfile(Openpose, selected_color)
    for m = 1:length(file2)
        for k = 1:length(file)
            
            C{k,m} = A{k,1} - B{m,1};
            if C{k,m}<0
                C{k,m} = -C{k,m};
            end
        end
    end
    
    [V,X] = min(cell2mat(C),[],1); % Is a row vector containing the minimum value of columns
    % V gives minimum value and X gives Index
    
    m = 1;
 
    for w= X
        
        depthDataBase = file3(w).name;
        rgbDataBase = file4(m).name;
        rgbDataBase2a = split(file5(m).name, "." );
        rgbDataBase2 = string(rgbDataBase2a(1));
        rgbDataBase3 = sprintf('%s.png', rgbDataBase2 );
        
        
        depthData = fullfile(depth_img, depthDataBase);
        rgbData = fullfile(Openpose, rgbDataBase);
        
        imageArrayy = imread(depthData);
        imageArrayy2 = imread(rgbData);
        
        depthData2 = fullfile(selected_depth, rgbDataBase3);
        imwrite(imageArrayy, depthData2);
        rgbData2 = fullfile(selected_color, rgbDataBase3);
        imwrite(imageArrayy2, rgbData2);
        %movefile(file4, file5) 
        
        
        m = m+1; % for part 2 m = m+1
    end
    
    
    %
    % PART 2:- If RGB images are more than depth then use the following code
else
    
    %copyfile(depth_img, selected_depth)
    for m = 1:length(file2)
        for k = 1:length(file)
            
            C{m,k} = A{k,1} - B{m,1};
            if C{m,k}<0
                C{m,k} = -C{m,k};
            end
        end
    end
    
    [V,X] = min(cell2mat(C),[],1); % Is a row vector containing the minimum value of columns
    % V gives minimum value and X gives Index

    w= 1;
    for m= X
        
        depthDataBase = file3(w).name;
        rgbDataBase = file4(m).name;
        rgbDataBase2 = file5(m).name;

        
        depthDataBasea = split(file3(w).name, "." );
        depthDataBase2 = string(depthDataBasea(1));
        depthDataBase3 = sprintf('%s.png', depthDataBase2 );
        
        depthData = fullfile(depth_img, depthDataBase);
        rgbData = fullfile(Openpose, rgbDataBase);
        
        imageArrayy = imread(depthData);
        imageArrayy2 = imread(rgbData);
        
        depthData2 = fullfile(selected_depth, depthDataBase3);
        imwrite(imageArrayy, depthData2);
        rgbData2 = fullfile(selected_color, depthDataBase3);
        imwrite(imageArrayy2, rgbData2);
        w = w+1;

    end
end
end
